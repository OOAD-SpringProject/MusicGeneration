from django.urls import path
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', csrf_exempt(views.homePage), name="homePage"),
    path('login/', csrf_exempt(views.login), name="login"),
    path('api/login', csrf_exempt(views.login), name="idk"),
    path('callback/', csrf_exempt(views.callback), name="callback"),
]
