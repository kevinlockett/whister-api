from rest_framework import serializers
from whistlerapi.models import AppUser

class AppUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppUser
        fields = ('id', 'username', 'full_name', 'first_name', 'last_name',
                  'address', 'city', 'state_id', 'state', 'zipcode', 'phone',
                  'email', 'bio', 'image', 'role_id', 'role', 'shop_id',
                  'shop', 'music_style_id', 'skill_level_id', 'instrument_id', 'instrument')
        depth = 2

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
    music_style_id = serializers.IntegerField()
    skill_level_id = serializers.IntegerField()
    instrument_id = serializers.IntegerField()
    
