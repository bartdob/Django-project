from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='poll-home'),
    path('create/', views.create, name='poll-create'),
    path('vote/<poll_id>', views.vote, name='poll-vote'),
    path('results/<poll_id>', views.results, name='poll-results'),
    path('delete/<int:poll_id>/', views.delete, name='poll-delete'),

]