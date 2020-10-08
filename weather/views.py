from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm
import os

def main(request):
    return render (request, 'main.html')


def index(request):
    key = os.environ.get('WEATHER_API_KEY')
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=9bb88af909d85a9aeff78756263783c7'


    errorMsg = ''
    message_class = '' # css class
    message = '' # msg for user

    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            newCity = form.cleaned_data['name']
            existingCity = City.objects.filter(name=newCity).count()

        if(existingCity == 0): #if city dont exist
            r = requests.get(url.format(newCity)).json()

            if r['cod'] == 200:
                form.save()
            else:
                errorMsg = "City dont exist at all"

        else:
            errorMsg = "city alredy added"



        if errorMsg:
            message = errorMsg
            message_class = 'is-danger'
        else:
            message = 'City added successfully!!!'
            message_class = 'is-success'

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temp': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'feels_like' : r['main']['feels_like'],
            'icon': r['weather'][0]['icon'],

        }

        weather_data.append(city_weather)


    context = {
        'weather_data' : weather_data,
        'form':form,
        'message' : message,
        'message_class' : message_class

        }

    return render(request, 'weather.html', context)

def deleteCity(request, cityName):
    City.objects.get(name=cityName).delete()

    return redirect('home')

# Create your views here.
