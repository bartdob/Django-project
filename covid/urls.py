from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_covid, name='covid'),
    path('update/', views.CovidUpdateView.as_view(), name='update'),
    path('graph/', views.HomeView.as_view(), name='cov-graph'),
    path('covid.csv/', views.export, name='export'),
]