from django.db import models

class SkillLevel(models.Model):
    level = models.CharField(max_length=20)

