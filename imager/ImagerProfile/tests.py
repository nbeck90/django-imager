from django.test import TestCase
from django.contrib.auth.models import User
from imagerprofile.models import ImagerProfile
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = factory.Sequence(lambda n: "User%03d" % n)


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ImagerProfile
        django_get_or_create = ('user',)

    user = factory.SubFactory(UserFactory)


class UserTestCase(TestCase):
    def setUp(self):
        """create two generic users with different settings"""
        User.objects.create(username='john_smith', is_active=False)
        User.objects.create(username='tom_thompson',
                            first_name='Tom', is_active=True)

    def test_user_has_username(self):
        """when user created, profile is created automatically"""
        john = User.objects.get(username='john_smith')
        tom = User.objects.get(username='tom_thompson')
        assert john.profile
        assert tom.profile

    def test_user_phone_number(self):
        """phone number can be added to profile"""
        tom = User.objects.get(username='tom_thompson')
        tom.profile.phone_number = '206-777-1234'
        tom.save()
        self.assertEqual(tom.profile.phone_number, '206-777-1234')

    def test_user_active(self):
        """is_active attribute of profile corretly refers to user property"""
        john = User.objects.get(username='john_smith')
        tom = User.objects.get(username='tom_thompson')
        assert tom.profile.is_active
        assert not john.is_active

    def test_profile_default(self):
        """default privacy setting for phone number set to false"""
        tom = User.objects.get(username='tom_thompson')
        assert tom.profile.phone_privacy is False

    def test_profile_active(self):
        """length of current active user list"""
        assert len(ImagerProfile.active.all()) == 1

    def test_user_follow_add(self):
        joe = UserFactory()
        fred = UserFactory()
        joe.profile.follow(fred.profile)
        assert fred.profile in joe.profile.following_user()

    def test_user_follow_delete(self):
        pass
