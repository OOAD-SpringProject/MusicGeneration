from django.shortcuts import render
from django.http import HttpResponse
from . import cred
import requests


# Create your views here.
def homePage(request):
    return render(request, 'spotify/home.html')

# Handling Spotify authorization here
def login(request):
    response = requests.get(cred.AUTH_URL, params=cred.parameters)
    print(response)
    print(response.content)
    return HttpResponse(response.content)

def callback(request):
    print("Made it into the callback function")
    return HttpResponse("Successfully made it back from the Spotify API")
