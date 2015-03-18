from django.test import TestCase, Client
from django.core import mail
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from imagerprofile.models import ImagerProfile
from selenium import selenium
import factory

import factory
import unittest


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
    # def setUp(self):
    #     """set up basic client"""
    #     self.client = Client()

    def loginHelper(self, username, password):
        return self.client.post('/login', {'username': username,
                                           'password': password})

    def test_home(self):
        """test that home page is available to logged out user"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        """test registration is available, and redirects on post"""
        username = 'sally'
        email = 'sally@sally.com'
        password = 'secret'
        response = self.client.get(reverse('registration_register'))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse('registration_register'), {
                'username': username,
                'email': email,
                'password': password
            })
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        """test login is reachable when not logged in,
        login changes auth"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        fred = UserFactory(username='fred', password='secret')
        self.loginHelper('fred', 'secret')
        assert fred.is_authenticated()

    def test_profile_view_redirect(self):
        """unauthenticated user redirected when trying
        to view personal profile"""
        # response = self.client.get('/logout')
        response = self.client.get('/profile')
        self.assertRedirects(response, '/login/', status_code=301)

    def test_profile_view(self):
        """authenticated user able to view personal profile"""
        fred = UserFactory(username='fred', password='secret')
        response = self.loginHelper('fred', 'secret')
        assert fred.is_authenticated()
        response = self.client.get('/profile')
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 200)
        assert 'Welcome, fred' in response.context['body']


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.user1 = UserFactory.create(
            username='alice',
            first_name='Alice',
            last_name='Restaurant')
        self.user1.set_password('secret')
        self.user1.save()
        self.user2 = UserFactory(username='Bob')
        self.selenium = webdriver.Firefox()
        super(TestLogin, self).setUp

    def tearDown(self):
        self.selenium.quit()
        super(TestLogin, self).tearDown()

    def login_user(self, user=None):
        if user is None:
            user = self.user1
        self.selenium.get(
            '{}{}'.format(self.live_server_url, reverse('auth_login'))
        )
        self.selenium.find_element_by_id('id_username').send_keys('alice')
        self.selenium.find_element_by_id('id_password').send_keys('secret')
        self.selenium.find_element_by_tag_name('form').submit()
