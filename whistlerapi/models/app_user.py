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

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        """Full name of Application User

        Returns:
            string: Gets the first and last name of the associated user object
        """
        return f"{self.authuser.first_name} {self.authuser.last_name}"
    
    @property
    def first_name(self):
        """First name of Application User

        Returns:
            string: Gets the first name of the associated user object
        """
        return f"{self.authuser.first_name}"
    
    @property
    def last_name(self):
        """Last name of Application User

        Returns:
            string: Gets the last name of the associated user object
        """
        return f"{self.authuser.last_name}"

    @property
    def email(self):
        """Application User email

        Returns:
            string: Email of associated user object
        """
        return self.authuser.email

    @property
    def username(self):
        """Username of Application User

        Returns:
            string: username of associated user object
        """
        return self.authuser.username
