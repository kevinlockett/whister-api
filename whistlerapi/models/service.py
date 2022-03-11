from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

class Service(models.Model):
    description = models.CharField(max_length=250)
    instrument = models.ForeignKey(
        'Instrument', on_delete=models.CASCADE)
    musicstyle = models.ForeignKey(
        'MusicStyle', on_delete=models.CASCADE, null=True, blank=True)
    price = models.FloatField(validators=[
        MinValueValidator(0.00), MaxValueValidator(17500.00)])
    servicedate = models.DateField()
    servicetype = models.ForeignKey(
        'ServiceType', on_delete=models.CASCADE, related_name='services')
    shop = models.ForeignKey(
        'Shop', on_delete=models.CASCADE, related_name='services')