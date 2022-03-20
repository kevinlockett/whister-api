from rest_framework import serializers
from whistlerapi.models import Instrument

class InstrumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instrument
        fields = ('id', 'name', 'family')
        depth = 1