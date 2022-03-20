from rest_framework import serializers
from whistlerapi.models import SkillLevel

class SkillLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = SkillLevel
        fields = ('id', 'level')
        depth = 1