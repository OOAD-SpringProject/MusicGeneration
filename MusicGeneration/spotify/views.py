from django.shortcuts import render
from django.http import HttpResponse
from . import cred
import requests



# Create your views here.
def homePage(request):
    return render(request, 'spotify/home.html')
def mainPage(request):
    return render(request, 'spotify/main.html')
def testPage(request):
    return render(request, 'spotify/test.html')
def instruction(request):
    return render(request, 'spotify/instruction.html')
def try1(request):
    return render(request, 'spotify/try1.html')
def base2(request):
    return render(request, 'spotify/base2.html')
def fall_login(request):
    return render(request, 'spotify/fall_login.html')
def succ_login(request):
    return render(request, 'spotify/succ_login.html')
def result(request):
    return render(request, 'spotify/result.html')

def base(request):
    return render(request, 'spotify/base.html')



# Handling Spotify authorization here
def login(request):
    response = requests.get(cred.AUTH_URL, params=cred.parameters)
    print(response)
    print(response.content)
    return HttpResponse(response.content)

def callback(request):
    print("Made it into the callback function")
    return HttpResponse("Successfully made it back from the Spotify API")
