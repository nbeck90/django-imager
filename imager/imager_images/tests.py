from django.test import TestCase
from imager_images.models import ImagerPhoto, ImagerAlbum
from imagerprofile.models import ImagerProfile
from imagerprofile.tests import UserFactory, ProfileFactory
from django.contrib.auth.models import User
import factory


# class UserFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = User
#         django_get_or_create = ('username',)

#     username = factory.Sequence(lambda n: "User%03d" % n)


# class ProfileFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = ImagerProfile
#         django_get_or_create = ('user',)

#     user = factory.SubFactory(UserFactory)


class ImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ImagerPhoto
        django_get_or_create = ('user',)

    picture = factory.django.ImageField(color='blue')
    user = factory.SubFactory(UserFactory)


class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ImagerAlbum
        django_get_or_create = ('user',)

    user = factory.SubFactory(UserFactory)


class ImageTestCase(TestCase):
    def test_image_in_album(self):
        album = AlbumFactory()
        image = ImageFactory()
        image.albums.add(album)
        image.save()
        assert image.albums.all()

    def test_image_has_user(self):
        image = ImageFactory()
        assert image.user

    def test(self):
        pass
