from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from imagerprofile.models import ImagerProfile


@receiver(post_save, sender=User)
def add_profile(sender, **kwargs):
    if kwargs['created']:
        obj = kwargs.get('instance')
        new_profile = ImagerProfile(user=obj)
        new_profile.save()
