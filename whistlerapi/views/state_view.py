from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from whistlerapi.models import State
from whistlerapi.serializers import StateSerializer, MessageSerializer

class StateView(ViewSet):

# swagger_auto_schema is a decorator that generates
# html documentation on (localhost:8000/swagger)
    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="The list of States",
                schema=StateSerializer(many=True)
            ),
        }
    )
    def list(self, request):
        """Get a list of States
        """
        states = State.objects.all()
        serializer = StateSerializer(states, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="The requested State",
                schema=StateSerializer()
            ),
            404: openapi.Response(
                description="State not found",
                schema=MessageSerializer()
            ),
        }
    )
    def retrieve(self, request, pk):
        """Get a single State by Id"""
        try:
            state = State.objects.get(pk=pk)
            serializer = StateSerializer(state)
            return Response(serializer.data)
        except State.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
