from datetime import datetime
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from whistlerapi.models import Invoice, PaymentType
from whistlerapi.serializers import (InvoiceSerializer,
                                     PayInvoiceSerializer, MessageSerializer)

class InvoiceView(ViewSet):

    # swagger_auto_schema is a decorator that generates html documentation
    # on (localhost:8000/swagger)

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
            description="The list of invoices for the current user",
            schema=InvoiceSerializer(many=True)
            ),
        }
    )
    def list(self, request):
        """Get a list of the current user's invoices
        """
        invoices = Invoice.objects.filter(customer_id=request.auth.user.id)
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        method='get',
        responses={
            200: openapi.Response(
                description="Returns the current user's open invoice",
                schema=InvoiceSerializer()
            ),
            404: openapi.Response(
                description="An open invoice was not found for the user",
                schema=MessageSerializer()
            ),
        }
    )
    @action(methods=['get'], detail=False)
    def current(self, request):
        """Get the user's current invoice"""
        try:
            invoice = Invoice.objects.get(
                completed_on=None, customer_id=request.auth.user.id)
            serializer = InvoiceSerializer(invoice)
            return Response(serializer.data)
        except Invoice.DoesNotExist:
            return Response({
                'message': 'You do not have an open invoice. Add a service to get started'},
                status=status.HTTP_404_NOT_FOUND
            )

    @swagger_auto_schema(
        method='put',
        request_body=PayInvoiceSerializer,
        responses={
            200: openapi.Response(
                description="Returns a message that the invoice was paid and is closed",
                schema=MessageSerializer()
            ),
            404: openapi.Response(
                description="Invoice or Payment Type not found and invoice remains open",
                schema=MessageSerializer()
            ),
        }
    )
    @action(methods=['put'], detail=True)
    def complete(self, request, pk):
        """Pay and close an invoice by adding a payment type and completed data
        """
        try:
            invoice = Invoice.objects.get(pk=pk, user=request.auth.user)
            payment_type = PaymentType.objects.get(
                pk=request.data['paymentTypeId'], customer=request.auth.user)
            invoice.payment_type = payment_type
            invoice.completed_on = datetime.now()
            invoice.save()
            return Response({'message': "Invoice paid and closed"},
                            status=status.HTTP_204_NO_CONTENT)
        except (Invoice.DoesNotExist, PaymentType.DoesNotExist) as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        responses={
            204: openapi.Response(
                description="No Content"
            ),
            404: openapi.Response(
                description="The invoice was not found",
                schema=MessageSerializer()
            ),
        }
    )
    def destroy(self, request, pk):
        """Delete an invoice, current user must be associated with the invoice to be deleted
        """
        try:
            invoice = Invoice.objects.get(pk=pk, user=request.auth.user)
            invoice.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Invoice.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
