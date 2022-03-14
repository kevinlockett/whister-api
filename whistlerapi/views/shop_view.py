from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from whistlerapi.models import Shop
from whistlerapi.serializers import ShopSerializer, MessageSerializer

class ShopView(ViewSet):

    @swagger_auto_schema(responses={
        200: openapi.Response(
            description="The list of Shops",
            schema=ShopSerializer(many=True)
        )
    })
    def list(self, request):
        """Get a list of Shop Styles
        """
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="The requested Shop",
                schema=ShopSerializer()
            ),
            404: openapi.Response(
                description="Shop not found",
                schema=MessageSerializer()
            ),
        }
    )
    def retrieve(self, request, pk):
        """Get a single Shop by Id"""
        try:
            shop = Shop.objects.get(pk=pk)
            serializer = ShopSerializer(shop)
            return Response(serializer.data)
        except Shop.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
