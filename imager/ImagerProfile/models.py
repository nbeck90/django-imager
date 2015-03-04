from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


class ActiveImagerManager(models.Manager):
    def get_queryset(self):
        return super(ActiveImagerManager,
                     self).get_queryset().filter(user__is_active=True)


@python_2_unicode_compatible
class ImagerProfile(models.Model):

    user = models.OneToOneField(User, related_name='profile')

    profile_picture = models.ImageField(null=True, blank=True,
                                        upload_to='images')

    phone_number = models.CharField(max_length=20, blank=True)

    birthday = models.DateField(null=True, blank=True)

    phone_privacy = models.BooleanField(default=False)
    birthday_privacy = models.BooleanField(default=False)
    picture_privacy = models.BooleanField(default=False)
    name_privacy = models.BooleanField(default=False)
    email_privacy = models.BooleanField(default=False)

    objects = models.Manager()
    active = ActiveImagerManager()

    following = models.ManyToManyField('self',
                                       symmetrical=False,
                                       null=True,
                                       related_name='+')
    blocking = models.ManyToManyField('self',
                                      symmetrical=False,
                                      null=True,
                                      related_name='+')

    def follow(self, imagerprofile):
        if self in imagerprofile.blocking.all():
            return 'User has blocked you'
        self.following.add(imagerprofile)

    def unfollow(self, imagerprofile):
        self.following.remove(imagerprofile)

    def block(self, imagerprofile):
        self.blocking.add(imagerprofile)

    def unblock(self, imagerprofile):
        self.blocking.remove(imagerprofile)

    def is_following(self):
        return self.following.all()

    def followers(self):
        return ImagerProfile.objects.filter(following=self)

    def blocked(self):
        return self.blocking.all()

    def __str__(self):
        return "User: {}".format(self.user.username)

    def is_active(self):
        return self.user.is_active()


@python_2_unicode_compatible
class ImagerAlbum(models.Model):
    user = models.OneToOneField(User, related_name='user')
    title = models.CharField(Default='MyAlbum')
    description = models.CharField(blank=True)
    date_created = models.DateField(null=True, blank=True)
    date_published = models.DateField(null=True, blank=True)
    date_modified = models.DateField(null=True, blank=True)
    cover = models.ImageField(null=True,
                              blank=True,
                              upload_to='images')


@python_2_unicode_compatible
class ImagerPhoto(models.Model):
    title = models.CharField(Default='MyAlbum')
    description = models.CharField(blank=True)
    date_uploaded = models.DateField(null=True, blank=True)
    date_published = models.DateField(null=True, blank=True)
    date_modified = models.DateField(null=True, blank=True)
    cover = models.ImageField(null=True,
                              blank=True,
                              upload_to='images')
    published = models.ChoiceField('Public', 'Private', 'Shared')
