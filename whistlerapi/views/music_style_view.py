from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from whistlerapi.models import MusicStyle
from whistlerapi.serializers import MusicStyleSerializer, MessageSerializer

class MusicStyleView(ViewSet):

    @swagger_auto_schema(responses={
        200: openapi.Response(
            description="The list of Music Styles",
            schema=MusicStyleSerializer(many=True)
        )
    })
    def list(self, request):
        """Get a list of Music Styles
        """
        musicstyles = MusicStyle.objects.all()
        serializer = MusicStyleSerializer(musicstyles, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="The requested Music Style",
                schema=MusicStyleSerializer()
            ),
            404: openapi.Response(
                description="Music Style not found",
                schema=MessageSerializer()
            ),
        }
    )
    def retrieve(self, request, pk):
        """Get a single Music Style by Id"""
        try:
            musicstyle = MusicStyle.objects.get(pk=pk)
            serializer = MusicStyleSerializer(musicstyle)
            return Response(serializer.data)
        except MusicStyle.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
