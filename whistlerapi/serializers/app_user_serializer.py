from rest_framework import serializers
from whistlerapi.models import AppUser

class AppUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppUser
        fields = ('username', 'full_name', 'address', 'city', 'state',
                  'zipcode', 'phone', 'bio', 'image', 'role', 'shop')
        depth = 1

class CreateAppUserSerializer(serializers.Serializer):

    class Meta:
        model = AppUser
        fields = ('username', 'password', 'first_name', 'last_name', 'email', 'address',
                  'city', 'state_id', 'zipcode', 'phone', 'bio', 'image', 'role_id',
                  'shop_id')
        depth = 1
