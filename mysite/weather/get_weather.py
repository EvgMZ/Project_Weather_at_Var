from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from .models import City, Weather


def wttr_weather_get(name_city):
    weather_parameters = {
        '0': '',
        'n': '',
        'Q': '',
        'format': 'j1'
    }
    response = requests.get(f'https://wttr.in/{name_city}', params=weather_parameters)
    if response.status_code == 200:
        weather = response.json()
        return weather


def yandex_weather_get(lat, long):
    url = f'https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={long}'
    headers = {
        'X-Yandex-API-Key': 'e1d85f08-832c-4765-8c42-13ea4a88e6f2'
    }
    response = requests.get(url, headers=headers)
    return response.json()

def main():
    yandex_weather_get()
    cities = City.objects.all()
    for city in cities:
        result_wttr = wttr_weather_get(city.name)
        temperature_wttr = result_wttr['current_condition'][0]['temp_C']
        weather_wttr = Weather.objects.create(temperature=temperature_wttr, id_city=city, data='wttr')
        weather_wttr.save()
        result_yandex = yandex_weather_get()
        temperature_yandex = result_yandex['fact']['temp']
        waether_yandex = Weather.objects.create(temperature=temperature_yandex, id_city=city, data='yandex')
        waether_yandex.save()