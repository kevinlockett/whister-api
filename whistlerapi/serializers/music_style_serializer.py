from rest_framework import serializers
from whistlerapi.models import MusicStyle

class MusicStyleSerializer(serializers.ModelSerializer):

    class Meta:
        model = MusicStyle
        fields = ('id', 'style')
        depth = 1
