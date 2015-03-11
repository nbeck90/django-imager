from django.shortcuts import render
# from django.core.exceptions import ObjectDoesNotExist
from imager_images.models import ImagerPhoto, ImagerAlbum, User
from imagerprofile.models import ImagerProfile


def home(request):
    try:
        random_photo = ImagerPhoto.random_photo.all()[0]
    except:
        random_photo = None
    return render(request, 'home.html', {
        'random_photo': random_photo
    })


def profile(request, username):
    # import pdb; pdb.set_trace()
    user = User.objects.get(username=username)
    try:
        albums = request.user.albums.all()
    except:
        albums = None
    profile = ImagerProfile.objects.get(user=user)
    return render(request, 'profile.html', {
        'albums': albums,
        'user': user,
        'profile': profile,
    })
