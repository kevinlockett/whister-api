from rest_framework import serializers
from whistlerapi.models import AppUser

class AppUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppUser
        fields = ('username', 'full_name', 'address', 'city', 'state',
                  'zipcode', 'phone', 'bio', 'image', 'role', 'shop')
        depth = 1

class CreateAppUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    address = serializers.CharField()
    city = serializers.CharField()
    state_id = serializers.IntegerField()
    zipcode = serializers.CharField()
    phone = serializers.CharField()
    bio = serializers.CharField()
    image = serializers.CharField()
    role_id = serializers.IntegerField()
    shop_id = serializers.IntegerField()
