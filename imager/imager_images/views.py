from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, UpdateView, DeleteView
from imager_images.models import ImagerPhoto, ImagerAlbum


class AlbumCreate(CreateView):
    model = ImagerAlbum
    context_object_name = 'album'
    success_url = '/profile/library/'
    fields = [
        'title',
        'description',
        'cover',
        'published'
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AlbumCreate, self).form_valid(form)

    def get_form(self, form_class):
        form = super(AlbumCreate, self).get_form(form_class)
        qs = form.fields['cover'].queryset
        form.fields['cover'].queryset = qs.filter(user=self.request.user)
        return form


class AlbumUpdate(UpdateView):
    model = ImagerAlbum
    context_object_name = 'album'
    success_url = '/profile/library/'
    fields = [
        'title',
        'description',
        'cover',
        'published'
    ]

    def get_form(self, form_class):
        form = super(AlbumUpdate, self).get_form(form_class)
        qs = form.fields['cover'].queryset
        form.fields['cover'].queryset = qs.filter(user=self.request.user)
        return form


class AlbumDelete(DeleteView):
    model = ImagerAlbum
    success_url = 'library'


class PhotoCreate(CreateView):
    model = ImagerPhoto
    context_object_name = 'photo'
    success_url = '/profile/library/'
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

    def get_form(self, form_class):
        form = super(PhotoCreate, self).get_form(form_class)
        qs = form.fields['albums'].queryset
        form.fields['albums'].queryset = qs.filter(user=self.request.user)
        return form


class PhotoUpdate(UpdateView):
    model = ImagerPhoto
    context_object_name = 'photo'
    success_url = '/profile/library/'
    fields = [
        'title',
        'picture',
        'description',
        'albums',
        'published'
    ]

    def get_form(self, form_class):
        form = super(PhotoUpdate, self).get_form(form_class)
        qs = form.fields['albums'].queryset
        form.fields['albums'].queryset = qs.filter(user=self.request.user)
        return form


class PhotoDelete(DeleteView):
    model = ImagerPhoto
    success_url = '/profile/library/'
