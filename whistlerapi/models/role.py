from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = 'roles'

    def __str__(self):
        return f'role: {self.name}'
