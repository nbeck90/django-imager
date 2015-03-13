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


class AlbumDelete(DeleteView):
    model = ImagerAlbum
    success_url = '/profile/'


class PhotoCreate(CreateView):
    # queryset = ImagerPhoto.objects.filter(albums__user=user)
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

    # def get_context_data(self, **kwargs):
    #     user = self.request.user
    #     context = super(PhotoCreate, self).get_context_data(**kwargs)
    #     context['albums'] = ImagerAlbum.objects.filter(user=user).all()
    #     return context


class PhotoDelete(DeleteView):
    model = ImagerPhoto
    success_url = '/profile/'
