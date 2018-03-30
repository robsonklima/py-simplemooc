from django.conf.urls import include, url

from django.contrib import admin
from django.urls import path

from simplemooc.courses import views

urlpatterns = [
    path('', views.courses, name='courses'),
    #url(r'^(?P<id>\d+)/$', views.details, name='details'),
    url(r'^(?P<slug>[\w_-]+)/$', views.details, name='details'),
]