from django.db import models

class Position(models.Model):
    position = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = 'Postions'

    def __str__(self):
        return f'Postion: {self.position}'