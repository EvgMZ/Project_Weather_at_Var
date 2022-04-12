from django.db import models

class City(models.Model):
    name = models.CharField(max_length=50)
    long = models.CharField(max_length=50)
    lat = models.CharField(max_length=50)


class Weather(models.Model):
    id_city = models.ForeignKey(City, on_delete=models.CASCADE)
    temperature = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    data = models.CharField(max_length=100)