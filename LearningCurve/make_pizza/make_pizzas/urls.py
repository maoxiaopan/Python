from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

# When URL request pass to make_pizza app level and matches the pattern we defined
# it will look for the views.index function we defined in views.py file
# then execute the function to return targeted html file
