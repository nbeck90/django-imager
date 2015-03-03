from django.test import TestCase
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'ImagerProfile.ImagerProfile'
        django_get_or_create = ('username',)

    username = 'John'
