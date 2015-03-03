from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class ImagerProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')

    profile_picture = models.ImageField(null=True, upload_to='images')
    picture_privacy = models.BooleanField(default=False)

    phone_number = models.CharField(max_length=15)  # X(XXX) XXX-XXXX
    phone_privacy = models.BooleanField(default=False)

    birthday = models.DateField()
    birthday_privacy = models.BooleanField(default=False)

    name_privacy = models.BooleanField(default=False)

    email_privacy = models.BooleanField(default=False)

    def __str__(self):
        return "User: {}".format(self.user.username)

    def is_active(self):
        return self.user.is_active()

    @classmethod
    def active(self):
        qs = self.get_queryset()
        return qs.filter(user__is_active=True)
