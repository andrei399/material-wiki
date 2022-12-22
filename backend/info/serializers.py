from rest_framework import serializers
from typing import Union  # noqa

# from backend import logger
from . import models

# TODO add serializer recursion for nested models


# Construct a serializer for all the models
class TopicCardSectionsListMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TopicCardSectionsListMemberModel
        fields = "__all__"


class TopicCardSectionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TopicCardSectionsListModel
        fields = "__all__"


class TopicCardSectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TopicCardSectionsModel
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImageModel
        fields = "__all__"


class TopicCardSerializer(serializers.ModelSerializer):
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
    # sub_chapters = serializers.SerializerMethodField(
    #     source="get_sub_chapters",
    # )
    class Meta:
        model = models.ChapterModel
        fields = "__all__"

    # def get_sub_chapters(self, obj):
    #     if obj.sub_chapters.count() == 0:
    #         print("No sub chapters")
    #         return None
    #     my_obj = obj.sub_chapters.all()[0]
    #     if my_obj.name == "test chapter 1_1":
    #         # print("Introduction")
    #         return ChapterSerializer(my_obj).data
    # print()

    # return ChapterSerializer(obj.sub_chapters.all(), many=True).data


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ItemModel
        fields = "__all__"


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuoteModel
        fields = "__all__"


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PageModel
        fields = "__all__"


def get_entry(model, id):
    if type(id) is list:
        return model.objects.filter(id__in=id).all()
    return model.objects.filter(id=id).first()
