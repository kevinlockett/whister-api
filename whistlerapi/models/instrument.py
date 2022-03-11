from django.db import models

class Instrument(models.Model):
    family = models.ForeignKey('InstrumentClass', on_delete=models.CASCADE)
    instrument = models.CharField(max_length=30)