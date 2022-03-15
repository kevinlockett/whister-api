from rest_framework import serializers
from whistlerapi.models import PaymentType

class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = ('id', 'obscured_num', 'merchant', 'customer', )
        depth = 1

class CreatePaymentTypeSerializer(serializers.Serializer):
    acct_number = serializers.CharField()
    merchant_id = serializers.IntegerField()
