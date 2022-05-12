from tkinter import W
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from datetime import  datetime
from .models import Weather, City
BASE_URL = './media/'
def asd():
    today = datetime.today()
    month = today.month
    dict_count_day = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    count_day = dict_count_day[month]
    now_day = today.day
    cities = City.objects.all()
    spisok_data = ['yandex', 'wttr', 'gismeteo']
    dict_data = {'yandex': [], 'wttr': [], 'gismeteo': []}
    plt.ioff()
    cnt_day = [i for i in range(1, now_day+7)]
    for city in cities:
        weathers = Weather.objects.filter(id_city=city.id)
        for data in spisok_data:
            spisok = []
            weathers_fil = weathers.filter(data=data)
            for weather in weathers_fil:
                spisok.append(float(weather.temperature))
            dict_data[data] = spisok
        plt.axis([1, now_day+1,  min(spisok)-2, max(spisok) +2])
        plt.title(f'{city.name} {count_day}')
        plt.plot(cnt_day, dict_data['yandex'],  'r.', cnt_day, dict_data['wttr'],'b.' , cnt_day, dict_data['gismeteo'], 'g.', linestyle='solid')
        lgnd = plt.legend(['yandex', 'wttr', 'gismeteo'], loc='best', shadow=True)
        plt.savefig(f'{BASE_URL}/{city.name}_{count_day}.png')
        plt.close()   