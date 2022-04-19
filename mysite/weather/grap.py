import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from datetime import  datetime
from .models import Weather
def asd():
    today = datetime.today()
    month = today.month
    dict_count_day = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    count_day = dict_count_day[month]
    now_day = today.day
    weather_data = Weather.objects.filter(data='yandex')
    print(weather_data.values('temperature')[0]['temperature'])
    plt.axis([1, now_day+1,  -60, 60])
    plt.title(count_day)
    #plt.plot(list(range(1, now_day)),), linewidth=2.0)
    plt.show()