from django.test import TestCase
from imager_images.models import ImagerPhoto, ImagerAlbum
from imagerprofile.models import ImagerProfile
from imagerprofile.tests import UserFactory, ProfileFactory
from django.contrib.auth.models import User
import factory


class ImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ImagerPhoto
        # django_get_or_create = ('picture',)
        # django_get_or_create = ('user',)

    picture = factory.django.ImageField(color='blue')
    # user = factory.SubFactory(UserFactory)


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
        user = UserFactory()
        image = ImageFactory()
        image.user = user
        image.save()
        assert image.user

    def test_user_remove_image(self):
        user = UserFactory()
        image = ImageFactory()
        image.user = user
        image.save()
        image.user = None
        image.save()
        assert not image.user

    def test_album_add_and_remove(self):
        image = ImageFactory()
        album = AlbumFactory()
        image.albums.add(album)
        album.cover = image
        album.save()
        assert album.cover
        assert image.albums

    def test_wrong_user(self):
        bob = UserFactory()
        sally = UserFactory()
        bobs_album = AlbumFactory(user=bob)
        sallys_image = ImageFactory()
        sallys_image.user = sally
        with self.assertRaises(AttributeError):
            sallys_image.albums.add(bobs_album)
