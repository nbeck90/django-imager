from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


PUBLIC = 'public'
PRIVATE = 'private'
SHARED = 'shared'

privacy_list = [(PUBLIC, 'Public'),
                (PRIVATE, 'Private'),
                (SHARED, 'Shared')]


# class PhotoManager(models.Manager):
#     # use_for_related_fields = True

#     def get_queryset(self):
#         return super(PhotoManager,
#                      self).get_queryset().filter(user__photos=True)


@python_2_unicode_compatible
class ImagerPhoto(models.Model):
    """image model"""
    user = models.ForeignKey(User, related_name='photos', null=True)
    title = models.CharField(default='MyPhoto', max_length=20)
    picture = models.ImageField(upload_to='images')
    albums = models.ManyToManyField('imager_images.ImagerAlbum',
                                    related_name='photos',
                                    blank=True,
                                    null=True)
    description = models.CharField(blank=True, max_length=20)
    date_uploaded = models.DateField(auto_now_add=True)
    date_published = models.DateField(null=True, blank=True)
    date_modified = models.DateField(auto_now=True)
    published = models.CharField(choices=privacy_list,
                                 default=PUBLIC,
                                 max_length=20)

    def __str__(self):
        return str(self.title)

    def image_tag(self):
        return u'<img src="/media/%s" width="50" height="50"/>' % self.picture
    image_tag.short_description = description
    image_tag.allow_tags = True


@python_2_unicode_compatible
class ImagerAlbum(models.Model):
    """photo album model"""
    user = models.ForeignKey(User, related_name='albums', null=True)
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

    # objects = models.Manager()
    # photos = ImagerPhoto()

    def add(self, photo):
        if self.user is photo.user:
            photo.albums.add(self)
        else:
            raise AttributeError

    def __str__(self):
        return str(self.title)
