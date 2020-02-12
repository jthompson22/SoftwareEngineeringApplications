from django.contrib import admin
from django.urls import path
from . import views 
from django.conf.urls import url, include

urlpatterns = [
    path('', views.home, name='home'),
]
