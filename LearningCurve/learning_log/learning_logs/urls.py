"""Define URL patterns for learning_logs"""
from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    # Home page
    path('', views.home, name='home')
    # ^ tells Python to look for the beginning of string
    # $ tells Python to look for the end of string
    # '^$' = '' equal to empty string
    # empty string matches base URL http://localhost:8000/, relative path
  #  url(r'^$', views.index, name = 'index')
]



