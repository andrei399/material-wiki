from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.core.files.storage import FileSystemStorage


class TopicCardSectionsListMemberModel(models.Model):
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value


class TopicCardSectionsListModel(models.Model):
    left = models.CharField(max_length=100)
    right = models.ManyToManyField(TopicCardSectionsListMemberModel)

    def __str__(self):
        return self.left


class TopicCardSectionsModel(models.Model):
    name = models.CharField(max_length=100)

    TEXT = "t"
    LIST = "l"
    CHOICES = (
        (TEXT, "text"),
        (LIST, "list"),
    )
    type = models.CharField(choices=CHOICES, max_length=10)

    expandable = models.BooleanField(default=False)
    text = models.CharField(max_length=1000, blank=True, null=True)
    list = models.ManyToManyField(TopicCardSectionsListModel, blank=True)

    def __str__(self):
        return self.name

    def get_type(self):
        for choice in self.CHOICES:
            if choice[0] == self.type:
                return choice[1]


fs = FileSystemStorage(location="/media/photos")


class ImageModel(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(
        upload_to=settings.MEDIA_ROOT,
    )
    links_to = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.name} in {settings.MEDIA_ROOT}"


class TopicCardModel(models.Model):
    title = models.CharField(max_length=200)
    image = models.ManyToManyField(ImageModel, blank=True)
    info = models.ManyToManyField(TopicCardSectionsModel, blank=True)

    def __str__(self):
        return self.title


class TextModel(models.Model):
    text = models.CharField(max_length=10000)

    def __str__(self):
        return self.text


class RowModel(models.Model):
    row = models.ManyToManyField(TextModel)

    def __str__(self):
        self.row.first().text


class TableModel(models.Model):
    rows = models.ManyToManyField(RowModel)

    def __str__(self):
        return self.rows.row.first().text


class SingleQuoteModel(models.Model):
    quote = models.CharField(max_length=10000)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.quote


class ChapterModel(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=10)

    TEXT = "tx"
    GALLERY = "g"
    TABLE = "ta"
    CHOICES = (
        (TEXT, "text"),
        (GALLERY, "gallery"),
        (TABLE, "table"),
    )

    type = models.CharField(choices=CHOICES, max_length=10)

    table = models.ForeignKey(
        TableModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    disclaimer = models.CharField(max_length=10000, blank=True, null=True)

    images = models.ManyToManyField(ImageModel, blank=True)

    text = models.CharField(max_length=10000, blank=True, null=True)
    quote = models.ForeignKey(
        SingleQuoteModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    sub_chapters = models.ManyToManyField(
        "self",
        blank=True,
        symmetrical=False,
    )

    def __str__(self):
        return self.name

    def get_type(self):
        for choice in self.CHOICES:
            if choice[0] == self.type:
                return choice[1]


class ItemModel(models.Model):
    name = models.CharField(max_length=100)
    quote = models.ForeignKey(
        SingleQuoteModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    about = models.CharField(max_length=10000)
    under_construction = models.BooleanField(default=False)
    chapter = models.ManyToManyField(ChapterModel, blank=True)
    card = models.ForeignKey(TopicCardModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class QuoteModel(models.Model):
    quotes = models.ManyToManyField(SingleQuoteModel)

    def __str__(self):
        return self.quotes.first().quote


class PageModel(models.Model):
    spoilers = models.BooleanField(default=False)
    big_name = models.CharField(max_length=100)
    items = models.ManyToManyField(ItemModel)
    quotes = models.ManyToManyField(QuoteModel, blank=True)
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.big_name)
        super(PageModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.big_name


class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    pages = models.ManyToManyField(PageModel, blank=True)

    def __str__(self):
        return self.name


class HomePageSectionModel(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=10000)
    image = models.ForeignKey(
        ImageModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    PAGE = "p"
    TEXT = "t"
    SIDE_TEXT = "st"
    SIDE_PAGE = "sp"
    CHOICES = (
        (PAGE, "page"),
        (TEXT, "text"),
        (SIDE_TEXT, "side_text"),
        (SIDE_PAGE, "side_page"),
    )
    type = models.CharField(choices=CHOICES, max_length=10)


class RelatedWikiModel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ForeignKey(
        ImageModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    link = models.CharField(max_length=1000)


class SocialMediaModel(models.Model):
    icon = models.CharField(max_length=100)
    link = models.CharField(max_length=1000)


class HomePageModel(models.Model):
    sections = models.ManyToManyField(HomePageSectionModel)
    left_sections = models.ManyToManyField(
        HomePageSectionModel,
        related_name="left_sections",
        blank=True,
    )
    related_wikis = models.ManyToManyField(RelatedWikiModel, blank=True)
    social_media = models.ManyToManyField(SocialMediaModel, blank=True)

    # TODO: Remove left sections, make sections be blank, restructure frontend to allow this kind of change # noqa


class FooterLinkModel(models.Model):
    text = models.CharField(max_length=100)
    link = models.CharField(max_length=1000)


class FooterSectionModel(models.Model):
    title = models.CharField(max_length=100)
    links = models.ManyToManyField(FooterLinkModel, blank=True)


class FooterModel(models.Model):
    image = models.ForeignKey(
        ImageModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    socials = models.ManyToManyField(SocialMediaModel, blank=True)
    extra = models.CharField(max_length=10000, blank=True, null=True)
    extra_img = models.ForeignKey(
        ImageModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="extra_img",
    )
    sections = models.ManyToManyField(FooterSectionModel, blank=True)
