from django.test import TestCase, Client
from django.core import mail
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from imagerprofile.models import ImagerProfile
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username', 'password', 'is_active')

    username = factory.Sequence(lambda n: "User%03d" % n)
    password = 'secret'
    is_active = True


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ImagerProfile
        django_get_or_create = ('user',)

    user = factory.SubFactory(UserFactory)


class LoginTestCase(TestCase):
    def setUp(self):
        """set up basic client"""
        self.client = Client()

    def loginHelper(self, username, password):
        return self.client.post('/login', {'username': username,
                                           'password': password})

    def test_home(self):
        """test that home page is available to logged out user"""
        response = self.client.get(reverse('home'))
        assert response.status_code == 200

    def test_register(self):
        """test registration is available, and redirects on post"""
        username = 'sally'
        email = 'sally@sally.com'
        password = 'secret'
        response = self.client.get(reverse('registration_register'))
        assert response.status_code == 200
        response = self.client.post(
            reverse('registration_register'), {
                'username': username,
                'email': email,
                'password': password
            })
        assert response.status_code == 200

    def test_login(self):
        """test login is reachable when not logged in,
        login changes auth"""
        response = self.client.get(reverse('login'))
        assert response.status_code == 200
        fred = UserFactory(username='fred', password='secret')
        self.loginHelper('fred', 'secret')
        assert fred.is_authenticated()

    def test_profile_view(self):
        """authenticated user able to view personal profile"""
        fred = UserFactory(username='fred', password='secret')
        self.loginHelper('fred', 'secret')
        assert fred.is_authenticated()
        response = self.client.get(reverse('profile'))
        assert response.status_code == 200
        assert 'Welcome, fred' in response.context['body']
