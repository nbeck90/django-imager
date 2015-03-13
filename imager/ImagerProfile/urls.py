from django.conf.urls import patterns, url
from imagerprofile.views import ImagerProfileUpdateView, profile

urlpatterns = patterns('',
    url(r'^$', profile, name='my_profile'),
    # url(r'^(?P<id>\d+)/', user_profile, name='profile'),
    url(r'^(?P<username>\w+)/edit/', ImagerProfileUpdateView.as_view(), name='profile_edit'),
)
