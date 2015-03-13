from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^upload/$', 'imager_images.views.PhotoCreate', name='upload'),
    url(r'^delete/$', 'imager_images.views.PhotoDelete', name='delete'),
    url(r'^album_create/$', 'imager_images.views.AlbumCreate', name='album_create'),
    url(r'^album_update/$', 'imager_images.views.AlbumUpdate', name='album_update'),
)
