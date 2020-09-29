from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main-page'),
    path('weather', views.index, name='weather'),
    path('delete/<cityName>/', views.deleteCity, name='deleteCity'),
]