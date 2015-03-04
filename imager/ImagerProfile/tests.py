from django.test import TestCase
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'imagerprofile.User'
        django_get_or_create = ('username',)

    username = factory.Sequence(lambda n: "Agent %03d" % n)
