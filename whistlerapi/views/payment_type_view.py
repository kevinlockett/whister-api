from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from whistlerapi.models import PaymentType
from whistlerapi.serializers import (
    CreatePaymentTypeSerializer, PaymentTypeSerializer, MessageSerializer)

class PaymentTypeView(ViewSet):

    @swagger_auto_schema(
        request_body=CreatePaymentTypeSerializer,
        responses={
            201: openapi.Response(
                description="Returns the created payment type",
                schema=PaymentTypeSerializer()
            ),
            400: openapi.Response(
                description="Validation Error",
                schema=MessageSerializer()
            ),
        }
    )
    def create(self, request):
        """Create a payment type for the current user"""
        try:
            payment_type = PaymentType.objects.create(
                customer=request.auth.user,
                merchant_id=request.data['merchant_id'],
                acct_number=request.data['acct_number']
            )
            serializer = PaymentTypeSerializer(payment_type)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="The list of payment types for the current user",
                schema=PaymentTypeSerializer(many=True)
            ),
        }
    )
    def list(self, request):
        """Get a list of payment types for the current user"""
        user=request.auth.user
        payment_types = PaymentType.objects.filter(customer=user)
        serializer = PaymentTypeSerializer(payment_types, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="The requested Payment Type",
                schema=PaymentTypeSerializer()
            ),
            404: openapi.Response(
                description="Payment Type not found",
                schema=MessageSerializer()
            ),
        }
    )
    def retrieve(self, request, pk):
        """Get a single Payment Type by Id"""
        try:
            paymenttype = PaymentType.objects.get(pk=pk)
            serializer = PaymentTypeSerializer(paymenttype)
            return Response(serializer.data)
        except PaymentType.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=CreatePaymentTypeSerializer,
        responses={
            204: openapi.Response(
                description="No Content",
            ),
            400: openapi.Response(
                description="Validation Error",
                schema=MessageSerializer()
            ),
            404: openapi.Response(
                description="The Payment Type was not found",
                schema=MessageSerializer()
            ),
        }
    )
    def update(self, request, pk):
        """Update a Payment Type"""
        paymenttype = PaymentType.objects.get(pk=pk)

        try:
            paymenttype.customer=request.auth.user
            paymenttype.merchant_id=request.data['merchant_id']
            paymenttype.acct_number=request.data['acct_number']
            paymenttype.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        except PaymentType.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        responses={
            204: openapi.Response(
                description="No content, payment type deleted successfully",
            ),
            404: openapi.Response(
                description="Payment type not found",
                schema=MessageSerializer()
            )
        }
    )
    def destroy(self, request, pk):
        """Delete a payment type"""
        try:
            payment_type = PaymentType.objects.get(pk=pk)
            payment_type.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except PaymentType.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
