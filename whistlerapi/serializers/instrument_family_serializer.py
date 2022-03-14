from rest_framework import serializers
from whistlerapi.models import InstrumentFamily

class InstrumentFamilySerializer(serializers.ModelSerializer):

    class Meta:
        model = InstrumentFamily
        fields = ('id', 'family')
        depth = 1