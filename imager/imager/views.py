from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.tempalte import RequestContext, loader


def stub(request, *args, **kwargs):
    body = 'Stub View\n\n'
    if args:
        body += 'Args: \n'
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += 'Kwargs: \n'
        body += "\n".join(["\t%s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type='text/plain')


def home(request):
    context = {name: 'bob'}
    return render(request, 'home.html', context)
