from django.conf.urls import include, url

from django.contrib import admin
from django.urls import path
from simplemooc.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contato/', views.contact, name='contact'),
]