from rest_framework import serializers
from whistlerapi.models import Invoice, PaymentType
from .payment_type_serializer import PaymentTypeSerializer

class InvoiceSerializer(serializers.ModelSerializer):
    payment_type = PaymentTypeSerializer()
    class Meta:
        model = Invoice
        fields = ('id', 'customer', 'services', 'created_on',
                  'completed_on', 'total', 'payment_type')
        depth = 2

class PayInvoiceSerializer(serializers.ModelSerializer):
    payment_type = serializers.IntegerField()

    class Meta:
        model = PaymentType
        fields = ('payment_type',)
