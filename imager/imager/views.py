from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from imager_images.models import ImagerPhoto


def home(request):
    random_photo = ImagerPhoto.random_photo.all()
    return render(request, 'home.html', {
        'random_photo': random_photo.picture
    })
