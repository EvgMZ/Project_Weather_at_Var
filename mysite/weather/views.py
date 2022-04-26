from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from . import get_weather, grap

def index(request):
    #get_weather.main()
    grap.asd()
    return HttpResponse("asd")