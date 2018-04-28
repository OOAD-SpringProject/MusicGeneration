from django.urls import path
from django.shortcuts import render

from . import views

urlpatterns = [
    path('', views.homePage, name="homePage"),
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
    path('login/', views.login, name="login"),
    path('api/login', views.login, name="idk"),
    path('callback/', views.callback, name="callback"),
]
