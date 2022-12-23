from rest_framework import serializers
from typing import Union  # noqa

# from backend import logger
from . import models


class TopicCardSectionsListMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TopicCardSectionsListMemberModel
        fields = "__all__"


class TopicCardSectionsListSerializer(serializers.ModelSerializer):
    right = TopicCardSectionsListMemberSerializer(many=True)

    class Meta:
        model = models.TopicCardSectionsListModel
        fields = "__all__"


class TopicCardSectionsSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    list = TopicCardSectionsListSerializer(many=True)

    class Meta:
        model = models.TopicCardSectionsModel
        fields = "__all__"

    def get_type(self, obj):
        return obj.get_type()


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImageModel
        fields = "__all__"


class TopicCardSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True)
    info = TopicCardSectionsSerializer(many=True)

    class Meta:
        model = models.TopicCardModel
        fields = "__all__"


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TextModel
        fields = "__all__"


class RowSerializer(serializers.ModelSerializer):
    row = TextSerializer(many=True)

    class Meta:
        model = models.RowModel
        fields = "__all__"


class TableSerializer(serializers.ModelSerializer):
    column_names = serializers.SerializerMethodField(
        source="get_column_names",
    )
    rows = RowSerializer(many=True)

    class Meta:
        model = models.TableModel
        fields = "__all__"

    def get_column_names(self, obj):
        # grab first row from rows
        return obj.rows.first().row.all().values_list("text", flat=True)


class SingleQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SingleQuoteModel
        fields = "__all__"


class ChapterSerializer(serializers.ModelSerializer):
    sub_chapters = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()
    images = ImageSerializer(many=True)
    quote = SingleQuoteSerializer()
    table = TableSerializer()

    class Meta:
        model = models.ChapterModel
        fields = "__all__"

    def get_type(self, obj):
        return obj.get_type()

    def get_sub_chapters(self, obj):
        if obj.sub_chapters.count() == 0:
            return None
        return ChapterSerializer(obj.sub_chapters.all(), many=True).data


class ItemSerializer(serializers.ModelSerializer):
    quote = SingleQuoteSerializer()
    chapter = ChapterSerializer(many=True)
    card = TopicCardSerializer()

    class Meta:
        model = models.ItemModel
        fields = "__all__"


class QuoteSerializer(serializers.ModelSerializer):
    quotes = SingleQuoteSerializer(many=True)

    class Meta:
        model = models.QuoteModel
        fields = "__all__"


class PageSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    quotes = QuoteSerializer(many=True)

    class Meta:
        model = models.PageModel
        fields = "__all__"


def get_entry(model, value=None, attribute=None):
    if attribute is None:
        attribute = "id"
    if type(value) is list:
        return model.objects.filter(id__in=id).all()
    return model.objects.filter(**{attribute: value}).first()
