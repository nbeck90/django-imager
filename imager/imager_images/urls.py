from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from imager_images.views import AlbumCreate, AlbumUpdate, PhotoCreate, PhotoDelete


urlpatterns = patterns('imager_images.views',
    url(r'^upload/$', login_required(PhotoCreate.as_view()), name='upload'),
    url(r'^delete/(?P<id>\d+)/$', login_required(PhotoDelete.as_view()), name='delete'),
    url(r'^album_create/$', login_required(AlbumCreate.as_view()), name='album_create'),
    url(r'^album_update/(?P<id>\d+)/$', login_required(AlbumUpdate.as_view()), name='album_update'),
)
