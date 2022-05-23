from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from whistlerapi.models import Role
from whistlerapi.serializers import RoleSerializer, MessageSerializer

class RoleView(ViewSet):

# swagger_auto_schema is a decorator that generates
# html documentation on (localhost:8000/swagger)
    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="The list of Roles",
                schema=RoleSerializer(many=True)
            ),
        }
    )
    def list(self, request):
        """Get a list of Roles
        """
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="The requested Role",
                schema=RoleSerializer()
            ),
            404: openapi.Response(
                description="Role not found",
                schema=MessageSerializer()
            ),
        }
    )
    def retrieve(self, request, pk):
        """Get a single Role by Id"""
        try:
            role = Role.objects.get(pk=pk)
            serializer = RoleSerializer(role)
            return Response(serializer.data)
        except Role.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
