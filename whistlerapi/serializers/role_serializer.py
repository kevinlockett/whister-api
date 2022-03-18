from rest_framework import serializers
from whistlerapi.models import Role

class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = ('id', 'name')
        depth = 1