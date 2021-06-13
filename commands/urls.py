from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('commands', views.commands, name="commands"),
    path('commands/api', views.api, name="commands"),
]