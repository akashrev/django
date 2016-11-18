from django.http import Http404, HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "It is now %s." % now
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #assert False
    html = "In %s hour(s), it will be  %s. " % (offset, dt)
    return HttpResponse(html)

from django.shortcuts import render

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})

def printnames(request):
    name = ['apple', 'mango', 'carrot', 'orange']
    return render(request, 'names.html', {'names': name})
