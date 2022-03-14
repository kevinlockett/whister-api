from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from whistlerapi.models import AppUser
from whistlerapi.serializers import AppUserSerializer, MessageSerializer, CreateAppUserSerializer

class AppUserView(ViewSet):

    @swagger_auto_schema(responses={
        200: openapi.Response(
            description="The list of AppUsers",
            schema=AppUserSerializer(many=True)
        )
    })
    def list(self, request):
        """Get a list of Application Users
        """
        appusers = AppUser.objects.all()
        serializer = AppUserSerializer(appusers, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="The requested Application User",
                schema=AppUserSerializer()
            ),
            404: openapi.Response(
                description="Application User not found",
                schema=MessageSerializer()
            ),
        }
    )
    def retrieve(self, request, pk):
        """Get a single Application User by Id"""
        try:
            appuser = AppUser.objects.get(pk=pk)
            serializer = AppUserSerializer(appuser)
            return Response(serializer.data)
        except AppUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=CreateAppUserSerializer,
        responses={
            204: openapi.Response(
                description="No Content",
            ),
            400: openapi.Response(
                description="Validation Error",
                schema=MessageSerializer()
            ),
            404: openapi.Response(
                description="The product was not found",
                schema=MessageSerializer()
            )
        }
    )
    def update(self, request, pk):
        """Update an Application User"""
        appuser = AppUser.objects.get(pk=pk)

        try:
            appuser.authuser.username = request.data['username']
            appuser.authuser.first_name = request.data['first_name']
            appuser.authuser.last_name = request.data['last_name']
            appuser.address = request.data['address']
            appuser.city = request.data['city']
            appuser.state_id = request.data['state_id']
            appuser.zipcode = request.data['zipcode']
            appuser.phone = request.data['phone']
            appuser.bio = request.data['bio']
            appuser.image = request.data['image']
            appuser.role_id = request.data['role_id']
            appuser.shop_id = request.data['shop_id']
            appuser.save()
            appuser.authuser.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        except AppUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        responses={
            204: openapi.Response(
                description="No Content",
            ),
            404: openapi.Response(
                description="The Application User was not found",
                schema=MessageSerializer()
            )
        })
    def destroy(self, request, pk):
        """Delete an Application User"""
        try:
            appuser = AppUser.objects.get(pk=pk)
            appuser.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except AppUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        