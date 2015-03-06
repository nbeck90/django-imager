from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from imagerprofile.models import ImagerProfile


@receiver(post_save, sender=User)
def add_profile(sender, instance, **kwargs):
    if kwargs['created']:
        # try:
        new_profile = ImagerProfile(user=instance)
        new_profile.save()
        # except:
        #     pass
