from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.core.exceptions import ObjectDoesNotExist
from imager_images.models import ImagerPhoto, ImagerAlbum, User
from django.views.generic import UpdateView, DetailView
from imagerprofile.models import ImagerProfile


class ImagerProfileDetailView(DetailView):
    model = ImagerProfile


class ImagerProfileUpdateView(UpdateView):
    model = ImagerProfile
    # form_class = ImagerProfileEditFeature


@login_required()
def profile(request):
    user = request.user
    try:
        albums = ImagerAlbum.objects.filter(user=user).all()
    except:
        albums = None
    profile = ImagerProfile.objects.get(user=user)
    following = len(profile.followers.all())
    num_photos = ImagerPhoto.objects.filter(user=user).count()
    return render(request, 'profile.html', {
        'albums': albums,
        'user': user,
        'profile': profile,
        'following': following,
        'num_album': len(albums),
        'num_photo': num_photos
    })


@login_required()
def user_profile(request, id):
    user = User.objects.get(id=id)
    try:
        albums = ImagerAlbum.objects.filter(user=user).all()
    except:
        albums = None
    profile = ImagerProfile.objects.get(user=user)
    following = len(profile.followers.all())
    num_photos = ImagerPhoto.objects.filter(user=user).count()
    return render(request, 'user_profile.html', {
        'albums': albums,
        'user': user,
        'profile': profile,
        'following': following,
        'num_album': len(albums),
        'num_photo': num_photos
    })
