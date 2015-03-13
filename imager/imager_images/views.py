from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from imagerprofile.models import ImagerProfile
from imager_images.models import ImagerPhoto, ImagerAlbum


class AlbumCreate(CreateView):
    model = ImagerAlbum


class AlbumUpdate(UpdateView):
    model = ImagerAlbum


class PhotoCreate(CreateView):
    model = ImagerPhoto


class PhotoDelete(DeleteView):
    model = ImagerPhoto
