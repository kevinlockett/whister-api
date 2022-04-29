from django.db import models

class Instrument(models.Model):
    family = models.ForeignKey(
        'InstrumentFamily', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
