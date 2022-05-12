from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import os
from . import get_weather, grap

def index(request):
    return render(request, 'index.html')

def reload(request):
    get_weather.main()
    grap.asd()
    return HttpResponse(request,{'message': 'ok'})
def moscow(request):
    return render(request, 'moscow.html')

def kazan(request):
    return render(request, 'kazan.html')

def sochi(request):
    return render(request, 'sochi.html')

def sevastopol(request):
    return render(request, 'sevastopol.html')

def ekaterinburg(request):
    return render(request, 'ekaterinburg.html')

def petersburg(request):
    return render(request, 'petersburg.html')

def novosibirsk(request):
    return render(request, 'novosibirsk.html')

def vladivostok(request):
    return render(request, 'vladivostok.html')