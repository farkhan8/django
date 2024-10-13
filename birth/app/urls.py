#create urls.py after startapp

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
]