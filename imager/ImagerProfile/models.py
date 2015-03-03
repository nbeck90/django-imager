from django.db import models
from django.contrib.auth.models import User


class ImagerProfile(models.Model):
    user = models.OneToOneField(User)

    profile_picture = models.ImageField(null=True)
    picture_privacy = models.BooleanField(default=False)

    phone_number = models.CharField(max_length=15)  # X(XXX) XXX-XXXX
    phone_privacy = models.BooleanField(default=False)

    birthday = models.DateField()  # null? blank=True?
    birthday_privacy = models.BooleanField(default=False)

    name_privacy = models.BooleanField(default=False)

    email_privacy = models.BooleanField(default=False)


# def is_active(self):
#     return self.user.is_active


# @classmethod
# def active_users(self):
#     qs = self.get_queryset()
#     return qs.filter(user_is_active=True)

# create profile
# delete user

# post_save.connect(create_profile, sender=User)
# pre_delete.conect(delete_user, sender=ImagerProfile)
