from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class ServiceType(models.Model):
    cost = models.FloatField(validators=[
        MinValueValidator(25.00), MaxValueValidator(1250.00)], default=25.00)
    service = models.CharField(max_length=25)
    class Meta:
        verbose_name_plural = 'Services'
    def __str__(self):
        return f'Service: {self.service}'
