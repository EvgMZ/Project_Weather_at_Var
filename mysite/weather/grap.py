from tkinter import W
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from datetime import  datetime
from .models import Weather, City
def asd():
    today = datetime.today()
    month = today.month
    dict_count_day = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    count_day = dict_count_day[month]
    now_day = today.day
    cities = City.objects.all()
    result_wtr  = []
    name_city = []
    spisok_data = ['yandex', 'wttr', 'gismeteto']
    for city in cities:
        weathers = Weather.objects.filter(id_city=city.id)
        spisok = []
        for data in spisok_data:
            weathers = weathers.filter(data=data)
            for weather in weathers:
                spisok.append(float(weather.temperature))
            print(f'{city.name} {data} {spisok}')
            plt.axis([1, now_day+1,  min(spisok)-2, max(spisok) +2])
            plt.title(f'{city.name} {count_day}')
            plt.plot(spisok)
            plt.savefig(f'{city.name}_{count_day}.png')
        plt.close()   
        result = {city.id : spisok}
        result_wtr.append(result)
    result_wtr[0][1]
    k = 1
    '''for i in range(len(result_wtr)):
        msc = result_wtr[i][k]
        plt.axis([1, now_day+1,  min(msc), max(msc)])
        plt.title(f'{name_city[i]} {count_day}')
        plt.plot(msc)
        plt.savefig(f'{name_city[i]}_{count_day}.png')
        #plt.close()
        k += 1'''