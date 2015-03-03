from django.db import models

# Create your models here.


class ImagerProfile(models.Model):

    profile_picture = models.ImageField()
    phone_number = models.CharField(max_length=15)  # X(XXX) XXX-XXXX
    birthday = models.DateField()
    picture_privacy = models.BooleanField()
    phone_privacy = models.BooleanField()
    birthday_privacy = models.BooleanField()
    name_privacy = models.BooleanField()
    email_privacy = models.BooleanField()
