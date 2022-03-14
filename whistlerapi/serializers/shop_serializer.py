from rest_framework import serializers
from whistlerapi.models import Shop

class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ('id', 'name', 'address', 'city', 'state', 'zipcode', 'phone', 'is_active')
        depth = 1