from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reload', views.reload, name='reload'),
    path('moscow', views.moscow, name='moscow'),
    path('kazan', views.kazan, name='kazan'),
    path('sochi', views.sochi, name='sochi'),
    path('sevastopol', views.sevastopol, name='sevastopol'),
    path('saint-petersburg', views.petersburg, name='petersburg'),
    path('ekaterinburg', views.ekaterinburg, name='ekaterinburg'),
    path('novosibirsk', views.novosibirsk, name='novosibirsk'),
    path('vladivostok', views.vladivostok, name='vladivostok'),
]
