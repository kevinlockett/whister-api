from rest_framework import serializers
from whistlerapi.models import ServiceType

class ServiceTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceType
        fields = ('id', 'service', 'cost')
        depth = 1