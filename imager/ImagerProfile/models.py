from django.db import models
from django.contrib.auth.models import User


# class ImagerProfile(models.Manager):
#     pass


class ImagerProfile(models.Model):
    user = models.OneToOneField(User)
    # objects = ImagerProfile()

    profile_picture = models.ImageField(null=True)
    phone_number = models.CharField(max_length=15)  # X(XXX) XXX-XXXX
    birthday = models.DateField()

    picture_privacy = models.BooleanField(default=False)
    phone_privacy = models.BooleanField(default=False)
    birthday_privacy = models.BooleanField(default=False)
    name_privacy = models.BooleanField(default=False)
    email_privacy = models.BooleanField(default=False)
