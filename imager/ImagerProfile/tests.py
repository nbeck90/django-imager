from django.test import TestCase
from django.contrib.auth.models import User
from imagerprofile.models import ImagerProfile
# import factory


# class UserFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = 'imagerprofile.User'
#         django_get_or_create = ('username',)

#     username = factory.Sequence(lambda n: "User%03d" % n)


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='john_smith', is_active=False)
        User.objects.create(username='tom_thompson',
                            first_name='Tom', is_active=True)

    def test_user_has_username(self):
        john = User.objects.get(username='john_smith')
        tom = User.objects.get(username='tom_thompson')
        assert john.profile
        assert tom.profile

    def test_user_phone_number(self):
        tom = User.objects.get(username='tom_thompson')
        tom.profile.phone_number = '206-777-1234'
        self.assertEqual(tom.profile.phone_number, '206-777-1234')

    def test_user_active(self):
        john = User.objects.get(username='john_smith')
        tom = User.objects.get(username='tom_thompson')
        assert tom.is_active
        assert not john.is_active

    def test_profile_default(self):
        tom = User.objects.get(username='tom_thompson')
        assert tom.profile.phone_privacy is False

    def test_profile_active(self):
        assert len(ImagerProfile.active.all()) == 1
