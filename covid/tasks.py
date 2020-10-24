from __future__ import absolute_import, unicode_literals
import requests
from django.conf import settings
from celery import task
from datetime import datetime, timedelta
import time
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery import Celery
from .models import Data

celery = Celery('tasks', broker='amqp://guest@localhost//') #!
import os

os.environ[ 'DJANGO_SETTINGS_MODULE' ] = "PROJECT.settings"

today = datetime.today()
today_str = datetime.today().strftime('%Y-%m-%d')
yesterday_str = (today - timedelta(days=6)).strftime('%Y-%m-%d')
today_day = (today.strftime('%y-%m-%d'))

@task
def get_covid_data(): #------------------------------------------ONE DAY------------------------------------------------
    today_str = datetime.today().strftime('%Y-%m-%d')
    urlP = 'https://api.covid19tracking.narrativa.com/api/%s/country/poland'%(today_str)

    headers = {
        'cache-control': "no-cache",
        'postman-token': "7cc0f843-c168-d269-3291-b07e948cbbdc"
        }

    responseP = requests.get(urlP, headers=headers)

    # if request.method == 'GET':
    resp_dP = responseP.json()
    today_new_deaths = resp_dP['dates'][today_str]['countries']['Poland']['today_new_deaths']
    today_new_confirmed = resp_dP['dates'][today_str]['countries']['Poland']['today_new_confirmed']
    today_new_recovered = resp_dP['dates'][today_str]['countries']['Poland']['today_new_recovered']
    source = resp_dP['dates'][today_str]['countries']['Poland']['source']
    api_date = resp_dP['dates'][today_str]['info']['date_generation']

    #--------------------------------------------TOTAL-------------------------------------------------
    url = "https://covid-19-data.p.rapidapi.com/country"

    querystring = {"format":"json","name":"Poland","province":"Poland"}

    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "218d1df78cmshaacd18448213d54p151669jsn4a235a652cd3"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)




    today_str, created = Data.objects.update_or_create(date=today_str, defaults={
            # 'date': api_date,
            # 'source': source,
            'title' : '0',
            'date' : today_str,
            'critical': 0,
            'deaths': 0,
            'today_new_deaths': today_new_deaths,
            'today_new_confirmed': today_new_confirmed,
            # 'today_new_recovered': today_new_recovered
    })


# @periodic_task(run_every=timedelta(seconds=30))
# # def get_all_covid_data():
#     # for data in Data.objects.all():
#     get_covid_data
#     print("-----------------------------------COVID--------------------")


@periodic_task(run_every=timedelta(seconds=30))
def every_30_seconds():
    print("Running periodic task!")
    get_covid_data()
    print("-----------------------------------COVID--------------------")