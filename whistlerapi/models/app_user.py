from django.db import models
from django.contrib.auth.models import User

class AppUser(models.Model):
    authuser = models.OneToOneField(
        User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    bio = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to='instructors',
        height_field=None, width_field=None,
        max_length=None, null=True, blank=True)
    phone = models.CharField(max_length=16)
    role = models.ForeignKey(
        'Role', related_name="role", on_delete=models.CASCADE)
    shop = models.ForeignKey(
        'Shop', related_name="shop", on_delete=models.CASCADE)
    state = models.ForeignKey(
        'State', related_name="state", on_delete=models.CASCADE)
    zipcode = models.CharField(max_length=9)
    