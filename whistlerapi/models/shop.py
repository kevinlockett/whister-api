from django.db import models

class Shop(models.Model):
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    is_active = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=16)
    state = models.ForeignKey(
        'State', on_delete=models.CASCADE)
    zipcode = models.CharField(max_length=9)
    