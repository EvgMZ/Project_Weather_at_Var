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
    for city in cities:
        weathers = Weather.objects.filter(id_city=city.id)
        name_city.append(city.name)
        spisok = []
        for weather in weathers:
            spisok.append(float(weather.temperature))
        result = {city.id : spisok}
        result_wtr.append(result)
    msc = result_wtr[0][1]
    print(msc)
    plt.axis([1, now_day+1,  min(msc), max(msc)])
    plt.title(count_day)
    plt.plot(msc)
    plt.show()