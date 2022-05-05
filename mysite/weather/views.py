from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import os
from . import get_weather, grap

def index(request):
    #get_weather.main()
    #grap.asd()
    print(os.getcwd())
    return render(request, 'index.html', {'url_image': 'D:\python_project\Project_Weather_at_Var\mysite\weather\media\Moscow_May.png'})