from django.db import models

class InstrumentFamily(models.Model):
    family = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = 'InstrumentFamilies'

    def __str__(self):
        return f'InstrumentFamily: {self.family}'
    