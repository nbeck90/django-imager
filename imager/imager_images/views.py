from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from imager_images.models import ImagerPhoto, ImagerAlbum


class AlbumCreate(CreateView):
    model = ImagerAlbum
    context_object_name = 'album'
    success_url = '/profile/'
    fields = [
        'title',
        'description',
        'cover',
        'published'
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AlbumCreate, self).form_valid(form)


class AlbumUpdate(UpdateView):
    model = ImagerAlbum
    context_object_name = 'album'
    success_url = '/profile/'
    fields = [
        'title',
        'description',
        'cover',
        'published'
    ]


class PhotoCreate(CreateView):
    model = ImagerPhoto
    context_object_name = 'photo'
    success_url = '/profile/'
    fields = [
        'title',
        'picture',
        'description',
        'albums',
        'published'
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PhotoCreate, self).form_valid(form)


class PhotoDelete(DeleteView):
    model = ImagerPhoto
    success_url = '/profile/'
