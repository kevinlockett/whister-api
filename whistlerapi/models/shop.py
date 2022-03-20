from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.ForeignKey(
        'State', on_delete=models.CASCADE)
    zipcode = models.CharField(max_length=9)
    phone = models.CharField(max_length=16)
