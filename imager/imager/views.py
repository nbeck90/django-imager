from django.shortcuts import render
from imager_images.models import ImagerPhoto


def home(request):
    try:
        random_photo = ImagerPhoto.random_photo.picture.url
    except:
        random_photo = None
    return render(request, 'home.html', {
        'random_photo': random_photo
    })
