from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('staff', views.staff, name="staff"),
    path('terms', views.terms, name="terms"),
    path('search',views.search, name='search')
]