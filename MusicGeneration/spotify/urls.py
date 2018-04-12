from django.urls import path
from django.shortcuts import render

from . import views

urlpatterns = [
    path('homePage/', views.homePage, name="homePage"),
    path('login/', views.login, name="login"),
    path('api/login', views.login, name="idk"),
    path('callback/', views.callback, name="callback"),
]
