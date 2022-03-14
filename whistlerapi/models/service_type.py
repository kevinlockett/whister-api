from django.db import models

class ServiceType(models.Model):
    service = models.CharField(max_length=25)
    class Meta:
        verbose_name_plural = 'Services'
    def __str__(self):
        return f'Service: {self.service}'
