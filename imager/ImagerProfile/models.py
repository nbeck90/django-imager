from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


class ActiveImagerManager(models.Manager):
    def get_queryset(self):
        return super(ActiveImagerManager, self).get_queryset().filter(user__is_active=True)


@python_2_unicode_compatible
class ImagerProfile(models.Model):

    user = models.OneToOneField(User, related_name='profile')

    profile_picture = models.ImageField(null=True, blank=True,
                                        upload_to='images')

    phone_number = models.CharField(max_length=15)  # X(XXX) XXX-XXXX

    birthday = models.DateField(null=True, blank=True)

    phone_privacy = models.BooleanField(default=False)
    birthday_privacy = models.BooleanField(default=False)
    picture_privacy = models.BooleanField(default=False)
    name_privacy = models.BooleanField(default=False)
    email_privacy = models.BooleanField(default=False)

    objects = models.Manager()
    active = ActiveImagerManager()

    def __str__(self):
        return "User: {}".format(self.user.username)

    def is_active(self):
        return self.user.is_active()

    following = models.ManyToManyField('self', symmetrical=False, required=False)

    def follow(self, ImagerProfile):
        self.following.add(ImagerProfile)

    def unfollow(self, other_profile):
        self.following.remove(other_profile.ImagerProfile)

    def following_user(self):
        return self.following.all()

    def followers(self):
        return ImagerProfile.objects.filter(following__id__=self.id)


# class Relationship(models.Model):

#     default = 0
#     follow = 1
#     friend = 2
#     block = 4

#     relationship_to = models.ForeignKey(ImagerProfile, related_name='+')
#     relationship_from = models.ForeignKey(ImagerProfile, related_name='+')
#     status = models.IntegerField()

#     def following(self):
#         return Relationship.objects.filter(left=self.user, status__in=(1, 3))

#     def followers(self):
#         return Relationship.objects.filter(right=self.user, status__in=(1, 3))
