from django.db import models

class MusicStyle(models.Model):
    style = models.CharField(max_length=25)
    class Meta:
        verbose_name_plural = 'MusicStyles'

    def __str__(self):
        return f'MusicStyle: {self.style}'
    