from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'address', 'city', 'state',
                  'zipcode', 'phone', 'shop', 'role', 'invoices')
        depth = 2

class CreateUserSerializer(serializers.Serializer):
        username = serializers.CharField()
        password = serializers.CharField(required=False)
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
        shop_id =serializers.IntegerField()
        
