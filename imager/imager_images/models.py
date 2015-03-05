from django.db import models
from django.contrib.auth.models import User

PUBLIC = 'public'
PRIVATE = 'private'
SHARED = 'shared'

privacy_list = [(PUBLIC, 'Public'),
                (PRIVATE, 'Private'),
                (SHARED, 'Shared')]


class ImagerPhoto(models.Model):
    title = models.CharField(default='MyPhoto', max_length=20)
    picture = models.ImageField(upload_to='images')
    albums = models.ManyToManyField('imager_images.ImagerAlbum',
                                    related_name='photos')
    description = models.CharField(blank=True, max_length=20)
    date_uploaded = models.DateField(auto_now_add=True)
    date_published = models.DateField(null=True, blank=True)
    date_modified = models.DateField(auto_now=True)
    published = models.CharField(choices=privacy_list,
                                 default=PUBLIC,
                                 max_length=20)

    def __str__(self):
        return str(self.title)


class ImagerAlbum(models.Model):
    user = models.ForeignKey(User, related_name='photos')
    title = models.CharField(default='MyAlbum', max_length=50)
    description = models.TextField(blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_published = models.DateField(null=True, blank=True)
    date_modified = models.DateField(auto_now=True)
    published = models.CharField(choices=privacy_list,
                                 default=PUBLIC,
                                 max_length=20)
    cover = models.ForeignKey(ImagerPhoto,
                              blank=True,
                              related_name='+',
                              null=True)

    def __str__(self):
        return str(self.title)
