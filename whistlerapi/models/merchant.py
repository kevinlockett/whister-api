from django.db import models

class Merchant(models.Model):
    name = models.CharField(max_length=50)
    