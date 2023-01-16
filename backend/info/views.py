from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from . import models, serializers


class PageModelView(ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.PageSerializer
    queryset = models.PageModel.objects.all()
    lookup_field = "slug"


class ImageView(ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.ImageSerializer
    lookup_field = "id"

    def get_queryset(self):
        print(self.kwargs)
        a = models.PageModel.objects.filter(slug=self.kwargs["slug"])
        a = a.first().items.filter(name=self.kwargs["name"]).first().card.image
        print(serializers.ImageSerializer(a.first()).data)
        return a


class SingleImageView(ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.ImageSerializer
    queryset = models.ImageModel.objects.all()
    lookup_field = "name"


class ItemView(ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.ItemSerializer
    queryset = models.ItemModel.objects.all()
    lookup_field = "id"


class HomePageView(ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.HomePageSerializer
    queryset = models.HomePageModel.objects.all()
    lookup_field = "id"


class RelatedWikiView(ModelViewSet):
    permissions_classes = (permissions.AllowAny,)
    serializer_class = serializers.RelatedWikiSerializer
    queryset = models.RelatedWikiModel.objects.all()
    lookup_field = "id"


class FooterView(ModelViewSet):
    permissions_classes = (permissions.AllowAny,)
    serializer_class = serializers.FooterSerializer
    queryset = models.FooterModel.objects.all()
    lookup_field = "id"


class HPSView(ModelViewSet):
    permissions_classes = (permissions.AllowAny,)
    serializer_class = serializers.HPSectionSerializer
    queryset = models.HomePageSectionModel.objects.all()
    lookup_field = "id"
