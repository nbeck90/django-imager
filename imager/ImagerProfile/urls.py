from django.conf.urls import patterns, url
from imager.views import ImagerProfileUpdateView, profile

urlpatterns = patterns(
    'imagerprofile.views',
    url(r'^$', profile, name='my_profile'),
    # url(r'^(?P<id>\d+)/', user_profile, name='profile'),
    url(r'^(?P<username>\w+)/edit/', ImagerProfileUpdateView.as_view(), name='profile_edit'),
)
