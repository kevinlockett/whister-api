from rest_framework import serializers
from whistlerapi.models import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'service_type', 'description', 'price', 'instrument', 'service_date', 'shop')
        depth = 2

class CreateServiceSerializer(serializers.Serializer):
    
    service_type_id = serializers.IntegerField()
    instrument_id = serializers.IntegerField()
    description = serializers.CharField()
    price = serializers.FloatField()
    service_date = serializers.DateTimeField()
    shop_id = serializers.IntegerField()
