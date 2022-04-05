from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests


def index(request):
    weather_parameters = {
        '0': '',
        'n': '',
        'Q': '',
        'format': 3
    }
    response = requests.get('https://wttr.in/Moscow', params=weather_parameters)
    if response.status_code == 200:
        weather = response.text
        return render(request, 'index.html', context={'weather': weather})
    else:
        return HttpResponse('Неверный запрос')
