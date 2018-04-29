from django.urls import path
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', csrf_exempt(views.homePage), name="homePage"),
    path('homePage/', csrf_exempt(views.homePage), name="homePage"),
    path('login/', csrf_exempt(views.login), name="login"),
    path('callback/', csrf_exempt(views.callback), name="callback"),
    path('result/', views.result, name="result"),
    path('instruction/', views.instruction, name="instruction"),
]
