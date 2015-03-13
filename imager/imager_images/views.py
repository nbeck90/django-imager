from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from imagerprofile.models import ImagerProfile
from imager_images.models import ImagerPhoto, ImagerAlbum


class AlbumCreateView(CreateView):
    model = ImagerAlbum


class AlbumUpdateView(UpdateView):
    model = ImagerAlbum


class PhotoCreateView(CreateView):
    model = ImagerPhoto


class PhotoDeleteView(DeleteView):
    model = ImagerPhoto
