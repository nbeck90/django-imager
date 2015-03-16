from django.conf.urls import patterns, include, url
from django.contrib import admin, auth
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    # Admin Routes
    url(r'^admin/', include(admin.site.urls)),

    # Reg Routes
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^login/', auth.views.login, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                      {'next_page': '/'}, name='logout'),

    # Main Routes
    url(r'^library/(?P<id>\d+)', 'imager.views.library', name='library'),
    url(r'^stream/(?P<id>\d+)', 'imager.views.stream', name='stream'),
    url(r'^$', 'imager.views.home', name='home'),
    url(r'^profile/', include('imagerprofile.urls')),
    url(r'^images/', include('imager_images.urls')),

)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
