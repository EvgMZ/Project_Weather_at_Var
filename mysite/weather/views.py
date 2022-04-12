from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from . import get_weather

def index(request):
    get_weather.main()