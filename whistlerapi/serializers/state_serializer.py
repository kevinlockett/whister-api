from rest_framework import serializers
from whistlerapi.models import State

class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = ('id', 'name', 'abbrev')
        depth = 1