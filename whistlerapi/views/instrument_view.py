from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from whistlerapi.models import Instrument
from whistlerapi.serializers import InstrumentSerializer, MessageSerializer

class InstrumentView(ViewSet):

    @swagger_auto_schema(responses={
        200: openapi.Response(
            description="The list of Instruments",
            schema=InstrumentSerializer(many=True)
        )
    })
    def list(self, request):
        """Get a list of Instruments
        """
        instruments = Instrument.objects.all()
        serializer = InstrumentSerializer(instruments, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="The requested Instrument",
                schema=InstrumentSerializer()
            ),
            404: openapi.Response(
                description="Instrument not found",
                schema=MessageSerializer()
            ),
        }
    )
    def retrieve(self, request, pk):
        """Get a single Instrument by Id"""
        try:
            instrument = Instrument.objects.get(pk=pk)
            serializer = InstrumentSerializer(instrument)
            return Response(serializer.data)
        except Instrument.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
