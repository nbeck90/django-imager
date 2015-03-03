from django.db import models
from django.contrib.auth.models import User


class ImagerProfile(models.Model):
    user = models.OneToOneField(User)

    profile_picture = models.ImageField(null=True)
    picture_privacy = models.BooleanField(default=False)

    phone_number = models.CharField(max_length=15)  # X(XXX) XXX-XXXX
    phone_privacy = models.BooleanField(default=False)

    birthday = models.DateField()
    birthday_privacy = models.BooleanField(default=False)

    name_privacy = models.BooleanField(default=False)

    email_privacy = models.BooleanField(default=False)
