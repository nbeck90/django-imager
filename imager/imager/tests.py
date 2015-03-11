from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from imagerprofile.models import ImagerProfile
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username', 'password')

    username = factory.Sequence(lambda n: "User%03d" % n)
    password = 'secret'


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ImagerProfile
        django_get_or_create = ('user',)

    user = factory.SubFactory(UserFactory)


class LoginTestCase(TestCase):
    def setUp(self):
        """set up basic client"""
        self.client = Client()

    # def loginHelper(self):
        # UserFactory(username='fred', password='secret')
        # return self.client.post('/login', {'username': 'fred',
        #                                    'password': 'secret'}
        #                         )

    def test_home(self):
        """test that home page is available to logged out user"""
        response = self.client.get(reverse('home'))
        assert response.status_code == 200

    def test_login(self):
        """test login is reachable when not logged in,
        login form changes auth"""
        UserFactory(username='fred', password='secret')
        response = self.client.get(reverse('login'))
        assert response.status_code == 200
        assert self.client.login(username='fred', password='secret')
