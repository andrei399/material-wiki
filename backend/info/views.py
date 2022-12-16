from rest_framework import generics, permissions
from rest_framework.response import Response

# from rest_framework.viewsets import ModelViewSet

# from backend import logger


class TestAPI(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        # logger.info("TestAPI.get()")
        print("TestAPI.get()")
        return Response({"message": " In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before final copy is available"})

