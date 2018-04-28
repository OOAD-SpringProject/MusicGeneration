from django.urls import path
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', csrf_exempt(views.homePage), name="homePage"),
    path('login/', csrf_exempt(views.login), name="login"),
    path('api/login', csrf_exempt(views.login), name="idk"),
    path('callback/', csrf_exempt(views.callback), name="callback"),

    path('homePage/', views.homePage, name="homePage"),
    path('testPage/', views.testPage, name="testPage"),
    path('base2/', views.base2, name="base2"),
    path('try1/', views.try1, name="try1"),
    path('fall_login/', views.fall_login, name="fall_login"),
    path('succ_login/', views.succ_login, name="succ_login"),
    path('result/', views.result, name="result"),

    path('base/', views.base, name="base"),
    path('instruction/', views.instruction, name="instruction"),
    path('mainPage/', views.mainPage, name="mainPage"),
]
