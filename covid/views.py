from django.shortcuts import render, redirect
import requests
from datetime import datetime, timedelta
import time
from django.contrib import messages
from django.http import HttpResponseRedirect
from .tasks import get_covid_data
from django.views.generic import UpdateView, ListView
from django.views import View
from .models import Data


today = datetime.today()
today_str = datetime.today().strftime('%Y-%m-%d')
yesterday_str = (today - timedelta(days=6)).strftime('%Y-%m-%d')
today_day = (today.strftime('%y-%m-%d'))

def main_covid(request):
    #--------------------------------------------TOTAL-------------------------------------------------
    url = "https://covid-19-data.p.rapidapi.com/country"

    querystring = {"format":"json","name":"Poland","province":"Poland"}

    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "218d1df78cmshaacd18448213d54p151669jsn4a235a652cd3"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    #------------------------------------------ONE DAY------------------------------------------------

    urlP = 'https://api.covid19tracking.narrativa.com/api/%s/country/poland'%(today_str)

    headers = {
        'cache-control': "no-cache",
        'postman-token': "7cc0f843-c168-d269-3291-b07e948cbbdc"
        }

    responseP = requests.get(urlP, headers=headers)



    # ------------------------------------------------------------------------------------------------

    if request.method == 'GET':
        resp_d = response.json()
        confirmed = resp_d[0]['confirmed']
        recovered = resp_d[0]['recovered']
        critical = resp_d[0]['critical']
        deaths = resp_d[0]['deaths']

    # -----------one day------------
        resp_dP = responseP.json()
        today_new_deaths = resp_dP['dates'][today_str]['countries']['Poland']['today_new_deaths']
        today_new_confirmed = resp_dP['dates'][today_str]['countries']['Poland']['today_new_confirmed']
        today_new_recovered = resp_dP['dates'][today_str]['countries']['Poland']['today_new_recovered']
        source = resp_dP['dates'][today_str]['countries']['Poland']['source']
        api_date = resp_dP['dates'][today_str]['info']['date_generation']

        if (today_new_deaths == 0):
            today_new_deaths = 'no data/check later'
        if (today_new_confirmed == 0):
            today_new_confirmed = 'no data/check later'
        if (today_new_recovered == 0):
            today_new_recovered = 'no data/check later'

        context = {
            'api_date': api_date,
            'source': source,
            'date' : today_str,
            'confirmed': confirmed,
            'recovered': recovered,
            'critical': critical,
            'deaths': deaths,
            'today_new_deaths': today_new_deaths,
            'today_new_confirmed':today_new_confirmed,
            'today_new_recovered': today_new_recovered

            }
    return render (request, 'covid/covid.html', context)

def home(request):
    context = {
        'datas': Data.objects.all()
    }
    return render(request, 'cov-graph.html', context)

class CovidUpdateView(View):
    def get(self, request, *args, **kwargs):
        data = City.objects.all()
        for city in cities:
            get_covid_data.delay(city.name)

        messages.add_message(request, messages.INFO,
                            'covid update task started.')
        return HttpResponseRedirect(reverse('cov'))

class HomeView(ListView):
    model = Data
    template_name = 'cov-graph.html'
    context_object_name = 'datas'


