from django.shortcuts import render
from django.urls import path

from . import views
app_name = 'contactme'
urlpatterns = [
    path('', views.contactme, name='contactme'),
]

# Create your views here.
