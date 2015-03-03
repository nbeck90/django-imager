from django.db import models
# from django.conf import settings

# Create your models here.


class ImagerProfile(models.Model):

    profile_picture = models.ImageField()
    # user = models.OneToOneField(settings.AUTH_USER_MODEL)
    phone_number = models.CharField(max_length=15)  # X(XXX) XXX-XXXX
    birthday = models.DateField()
    picture_privacy = models.BooleanField()
    phone_privacy = models.BooleanField()
    birthday_privacy = models.BooleanField()
    name_privacy = models.BooleanField()
    email_privacy = models.BooleanField()
