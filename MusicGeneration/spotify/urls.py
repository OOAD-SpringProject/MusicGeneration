from django.urls import path
from django.shortcuts import render

from . import views

urlpatterns = [
    path('homePage/', views.homePage, name="homePage"),
    path('testPage/', views.testPage, name="testPage"),

    path('mainPage/', views.mainPage, name="mainPage"),
    path('login/', views.login, name="login"),
    path('api/login', views.login, name="idk"),
    path('callback/', views.callback, name="callback"),
]
