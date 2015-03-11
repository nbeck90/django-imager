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
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),

    # Main Routes
    url(r'^$', 'imager.views.home', name='home'),
    url(r'^profile/(?P<username>\w+)', 'imager.views.profile', name='profile'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if debug: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
