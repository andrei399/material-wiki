from rest_framework import generics, permissions
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet
from . import models, serializers

from backend import logger


class TestAPI(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        logger.info("TestAPI.get()")
        message = {
            "title": "Geralt of Rivia",
            "img": "https://i.imgur.com/92cNLxg.jpg",
            "info": {
                "0": {
                    "title": "Basic Information",
                    "type": "list",
                    "expanded": True,
                    "expandable": False,
                    "values": [
                        {
                            "title": "Allias(es)",
                            "values": [
                                "White Wolf",
                                "Gwynbleidd",
                                "White One",
                                "Butcher of Blaviken",
                                "Ravix of Fourhorn",
                                "Geralt Roger Eric du Haute-Bellegarde (the first name he wanted)",
                            ],
                        },
                        {"title": "Hair Color", "values": ["Milk-white"]},
                        {
                            "title": "Eye Color",
                            "values": [
                                "Dark, unspecified color(books)",
                                "Green(comics, The Hexer)",
                                "Golden(games, Netflix's The Witcher)",
                            ],
                        },
                        {"title": "Skin", "values": ["Pale"]},
                        {"title": "Race", "values": ["Human"]},
                        {"title": "Gender", "values": ["Male"]},
                    ],
                },
                "1": {
                    "title": "Physical Description",
                    "expanded": True,
                    "expandable": False,
                    "type": "list",
                    "values": [
                        {"title": "Title(s)", "values": ["Knight (knighted by Meve)"]},
                        {"title": "Profession", "values": ["Witcher"]},
                        {"title": "Affiliation(s)", "values": ["Wolf School"]},
                        {
                            "title": "Abilities",
                            "values": [
                                "Superhuman abilities",
                                "Swordsmanship",
                                "Alchemy",
                                "Signs",
                            ],
                        },
                    ],
                },
                "2": {
                    "title": "Family",
                    "expandable": True,
                    "expanded": False,
                    "type": "list",
                    "values": [
                        {
                            "title": "Parent(s)",
                            "values": ["Visenna (mother)", "Korin (father)"],
                        },
                        {
                            "title": "Partner(s)",
                            "values": [
                                "Yennefer (Love of his life in books, possible lover in The Witcher 3)",
                                "Triss Merigold (former lover in books, possible lover in all three games)",
                            ],
                        },
                        {"title": "Child(ren)", "values": ["Ciri (adopted daughter)"]},
                    ],
                },
            },
        }

        return Response(message)


class PageModelView(ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.PageSerializer
    queryset = models.PageModel.objects.all()
    lookup_field = "slug"
