from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_covid, name='covid'),
    path('update/', views.CovidUpdateView.as_view(), name='update'),
    path('cov/', views.HomeView.as_view(), name='cov'),
    path('graph/', views.home, name='covid-graph')

]