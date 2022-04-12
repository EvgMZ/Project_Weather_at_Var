from django.contrib import admin
from .models import City, Weather

class CityAdmin(admin.ModelAdmin):
    list_display = ('name','long','lat')
class WeatherAdmin(admin.ModelAdmin):
    list_display = ('id_city','temperature', 'date','data')

admin.site.register(City, CityAdmin)
admin.site.register(Weather, WeatherAdmin)