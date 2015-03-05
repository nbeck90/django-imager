from django.db import models
from django.contrib.auth.models import User

PUBLIC = 'public'
PRIVATE = 'private'
SHARED = 'shared'

privacy_list = [(PUBLIC, 'Public'),
                (PRIVATE, 'Private'),
                (SHARED, 'Shared')]


class ImagerAlbum(models.Model):
    user = models.OneToOneField(User, related_name='user')
    title = models.CharField(default='MyAlbum', max_length=50)
    description = models.TextField(blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_published = models.DateField(null=True, blank=True)
    date_modified = models.DateField(null=True, blank=True)
    published = models.CharField(choices=privacy_list,
                                 default=PUBLIC,
                                 max_length=20)

    def make_cover(self):
        photos = self.photos.all().image.name
        choices = ()
        for path in photos:
            choices + ((path, path.split('/')[-1]),)
        return choices

    cover = models.ForeignKey(blank=True, related_name='photos')


class ImagerPhoto(models.Model):
    title = models.CharField(default='MyAlbum', max_length=20)
    picture = models.ImageField(null=True, blank=True,
                                upload_to='images')
    albums = models.ManyToManyField(ImagerAlbum, related_name='photos')
    description = models.CharField(blank=True, max_length=20)
    date_uploaded = models.DateField(null=True, blank=True)
    date_published = models.DateField(null=True, blank=True)
    date_modified = models.DateField(null=True, blank=True)
    published = models.CharField(choices=privacy_list,
                                 default=PUBLIC,
                                 max_length=20)
