from django.db import models
from django.contrib.auth.models import User
class AppUser(models.Model):
    authuser = models.OneToOneField(
        User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.ForeignKey(
        'State', related_name="state", on_delete=models.CASCADE)
    zipcode = models.CharField(max_length=9)
    phone = models.CharField(max_length=16)
    image = models.ImageField(
        upload_to='instructors',
        height_field=None, width_field=None,
        max_length=None, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    shop = models.ForeignKey(
        'Shop', related_name="shop", on_delete=models.CASCADE)
    role = models.ForeignKey(
        'Role', related_name="role", on_delete=models.CASCADE)
    skill_level = models.ForeignKey(
        'SkillLevel', related_name="shop", on_delete=models.CASCADE, null = True)
    music_style = models.ForeignKey(
        'MusicStyle', related_name="role", on_delete=models.CASCADE, null = True)
    instrument = models.ForeignKey(
        'Instrument', on_delete=models.CASCADE, null=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

    @property
    def username(self):
        """Username of Application User

        Returns:
            string: username of associated user object
        """
        return self.authuser.username

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
