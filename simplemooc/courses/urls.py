from django.conf.urls import include, url

from django.contrib import admin
from django.urls import path

from simplemooc.courses import views

urlpatterns = [
    path('', views.courses, name='courses')
]