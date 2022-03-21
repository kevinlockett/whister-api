from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
class Service(models.Model):
    description = models.CharField(max_length=250)
    price = models.FloatField(validators=[
        MinValueValidator(50.00), MaxValueValidator(200.00)])
    service_date = models.DateTimeField()
    service_type = models.ForeignKey(
        'ServiceType', on_delete=models.CASCADE, related_name='services')
    shop = models.ForeignKey(
        'Shop', on_delete=models.CASCADE, related_name='services')
    