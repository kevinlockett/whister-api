from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from whistlerapi.models import Service, Invoice
from whistlerapi.serializers import CreateServiceSerializer,ServiceSerializer, MessageSerializer

class ServiceView(ViewSet):

# swagger_auto_schema is a decorator that generates
# html documentation on (localhost:8000/swagger)
    @swagger_auto_schema(
        request_body=CreateServiceSerializer,
        responses={
            201: openapi.Response(
                description="Returns the created service",
                schema=ServiceSerializer()
            ),
            400: openapi.Response(
                description="Validation Error",
                schema=MessageSerializer()
            ),
        }
    )
    def create(self, request):
        """Create a Service for the current user"""
        try:
            service = Service.objects.create(
                shop_id=request.data['shop_id'],
                servicetype_id=request.data['servicetype_id'],
                description=request.data['description'],
                price=request.data['price'],
                instrument_id=request.data['instrument_id'],
                service_date=request.data['service_date']
            )
            serializer = ServiceSerializer(service)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="The list of Services",
                schema=ServiceSerializer(many=True)
            ),
        },
        manual_parameters=[
            openapi.Parameter(
                "service_type",
                openapi.IN_QUERY,
                required=False,
                type=openapi.TYPE_INTEGER,
                description="Get services by service type"
            ),

            openapi.Parameter(
                "shop",
                openapi.IN_QUERY,
                required=False,
                type=openapi.TYPE_INTEGER,
                description="Get services based on shop"
            ),
        ]
    )
    def list(self, request):
        """Get a list of Services
        """
        services = Service.objects.all()

        service_type = request.query_params.get('service_type', None)
        shop = request.query_params.get('shop', None)

        if service_type is not None:
            services = services.filter(service_type_id=service_type)

        if shop is not None:
            services = services.filter(shop_id=shop)

        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="The requested Service",
                schema=ServiceSerializer()
            ),
            404: openapi.Response(
                description="Service not found",
                schema=MessageSerializer()
            ),
        }
    )
    def retrieve(self, request, pk):
        """Get a single Service by Id"""
        try:
            service = Service.objects.get(pk=pk)
            serializer = ServiceSerializer(service)
            return Response(serializer.data)
        except Service.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=CreateServiceSerializer,
        responses={
            204: openapi.Response(
                description="No Content",
            ),
            400: openapi.Response(
                description="Validation Error",
                schema=MessageSerializer()
            ),
            404: openapi.Response(
                description="The service was not found",
                schema=MessageSerializer()
            ),
        }
    )
    def update(self, request, pk):
        """Update a Service"""
        service = Service.objects.get(pk=pk)

        try:
            service.shop_id=request.data['shop_id']
            service.servicetype_id=request.data['servicetype_id']
            service.description=request.data['description']
            service.price=request.data['price']
            service.musicstyle_id=request.data['musicstyle_id']
            service.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        except Service.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        responses={
            204: openapi.Response(
                description="No Content",
            ),
            404: openapi.Response(
                description="The Service was not found",
                schema=MessageSerializer()
            ),
        }
    )
    def destroy(self, request, pk):
        """Delete a service"""
        try:
            service = Service.objects.get(pk=pk)
            service.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Service.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        method='POST',
        responses={
            201: openapi.Response(
                description="Returns message that service was added to invoice",
                schema=MessageSerializer()
            ),
            404: openapi.Response(
                description="Service not found",
                schema=MessageSerializer()
            ),
        }
    )
    @action(methods=['post'], detail=True)
    def add_to_invoice(self, request, pk):
        """Add a service to the current users open invoice"""
        try:
            service = Service.objects.get(pk=pk)
            invoice, _ = Invoice.objects.get_or_create(
                customer=request.auth.user_id, completed_on=None, payment_type=None)
            invoice.services.add(service)
            return Response({'message': 'service added'}, status=status.HTTP_201_CREATED)
        except Service.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        method='DELETE',
        responses={
            201: openapi.Response(
                description="Returns message that service was deleted from the invoice",
                schema=MessageSerializer()
            ),
            404: openapi.Response(
                description="Either the Service or Invoice was not found",
                schema=MessageSerializer()
            ),
        }
    )
    @action(methods=['delete'], detail=True)
    def remove_from_invoice(self, request, pk):
        """Remove a service from the user's open invoice"""
        try:
            service = Service.objects.get(pk=pk)
            invoice = Invoice.objects.get(
                user=request.auth.user, completed_on=None)
            invoice.services.remove(service)
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Service.DoesNotExist as ex:
            return Response(
                {'Product does not exist': ex.args[0]},
                status=status.HTTP_404_NOT_FOUND)
        except Invoice.DoesNotExist as ex:
            return Response(
                {'Invoice does not exist': ex.args[0]},
                status=status.HTTP_404_NOT_FOUND)
