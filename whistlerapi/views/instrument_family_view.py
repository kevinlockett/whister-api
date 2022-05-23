from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from whistlerapi.models import InstrumentFamily
from whistlerapi.serializers import InstrumentFamilySerializer, MessageSerializer

class InstrumentFamilyView(ViewSet):
# swagger_auto_schema is a decorator that generates html documentation on (localhost:8000/swagger)
    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="The list of Instrument Families",
                schema=InstrumentFamilySerializer(many=True)
            ),
        }
    )
    def list(self, request):
        """Get a list of Instrument Families
        """
        instrumentfamilies = InstrumentFamily.objects.all()
        serializer = InstrumentFamilySerializer(instrumentfamilies, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="The requested Instrument Family",
                schema=InstrumentFamilySerializer()
            ),
            404: openapi.Response(
                description="Instrument Family not found",
                schema=MessageSerializer()
            ),
        }
    )
    def retrieve(self, request, pk):
        """Get a single Music Style by Id"""
        try:
            instrumentfamily = InstrumentFamily.objects.get(pk=pk)
            serializer = InstrumentFamilySerializer(instrumentfamily)
            return Response(serializer.data)
        except InstrumentFamily.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
