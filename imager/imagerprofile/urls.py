from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from imagerprofile.views import (ImagerProfileUpdateView, profile,
                                 user_profile, library, stream)

urlpatterns = patterns('',
    url(r'^$', profile, name='my_profile'),
    url(r'^library/$', library, name='library'),
    url(r'^stream/$', stream, name='stream'),
    url(r'^(?P<id>\d+)/$', user_profile, name='profile'),
    url(r'^(?P<pk>\d+)/edit/$',
        login_required(ImagerProfileUpdateView.as_view()),
        name='profile_edit'),
)
