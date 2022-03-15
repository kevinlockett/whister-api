from rest_framework import serializers
from whistlerapi.models import Service

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ('id', 'shop', 'servicetype', 'description', 'price', 'instrument', 'musicstyle')
        depth = 1

class CreateServiceSerializer(serializers.Serializer):
    shop_id = serializers.IntegerField()
    servicetype_id = serializers.IntegerField()
    description = serializers.CharField()
    price = serializers.FloatField()
    instrument_id = serializers.IntegerField()
    musicstyle_id = serializers.IntegerField()
