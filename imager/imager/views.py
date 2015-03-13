from django.shortcuts import render
# from django.core.exceptions import ObjectDoesNotExist
from imager_images.models import ImagerPhoto, User, ImagerAlbum
from django.views.generic import ListView, UpdateView, DetailView
from imagerprofile.models import ImagerProfile
# from imagerprofile.forms import ImagerProfileEditFeature


def home(request):
    try:
        random_photo = ImagerPhoto.random_photo.all()[0]
    except:
        random_photo = None
    return render(request, 'home.html', {
        'random_photo': random_photo
    })


class ImagerProfileListView(DetailView):
    model = ImagerProfile


class ImagerProfileUpdateView(UpdateView):
    model = ImagerProfile
    # form_class = ImagerProfileEditFeature


def profile(request):
    # import pdb; pdb.set_trace()
    user = request.user
    try:
        albums = request.user.albums.filter(user=user).all()
    except:
        albums = None
    profile = ImagerProfile.objects.get(user=user)
    following = len(profile.followers.all())
    photos = ImagerPhoto.objects.filter(user=user).count()
    return render(request, 'profile.html', {
        'albums': albums,
        'user': user,
        'profile': profile,
        'following': following,
        'num_album': len(albums),
        'num_photo': photos
    })


def library(request, id):
    user = User.objects.get(pk=id)
    try:
        albums = request.user.albums.filter(user=user).all()
    except:
        albums = None
    try:
        photos = ImagerPhoto.objects.filter(user=user).all()
    except:
        photos = None
    return render(request, 'library.html', {
        'user': user,
        'albums': albums,
        'photos': photos
    })


def stream(request, id):
    # import pdb; pdb.set_trace()
    user = User.objects.get(pk=id)
    try:
        my_albums = request.user.albums.filter(user=user).all()
    except:
        my_albums = None
    try:
        followed_albums = ImagerAlbum.objects.filter(user=user.profile.is_following()).all()
    except:
        followed_albums = None
    try:
        photos = ImagerPhoto.objects.filter(user=user).all()
    except:
        photos = None
    return render(request, 'stream.html', {
        'user': user,
        'my_albums': my_albums,
        'followed_albums': followed_albums,
        'photos': photos
    })
