from django.db import models

class InstrumentClass(models.Model):
    family = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = 'InstrumentFamilies'

    def __str__(self):
        return f'Family: {self.family}'