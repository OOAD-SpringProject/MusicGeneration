import spotipy
import spotipy.util as util
import random
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, Template
from . import cred
from .classes import usernameForm
import requests


# Create your views here.
def homePage(request):
    return render(request, 'spotify/home.html')

# Handling Spotify authorization here
def login(request):
    if request.method == 'POST':
        form = usernameForm(request.POST)
        if form.is_valid():
            userID = form.cleaned_data['userID']
            print(userID)
            token = util.prompt_for_user_token(userID, cred.SCOPE, client_id=cred.CLIENT_ID, client_secret=cred.CLIENT_SECRET, redirect_uri=cred.REDIRECT_URI)
            if token:
                sp = spotipy.Spotify(auth=token)
                playlists = sp.user_playlists(userID)
                for playlist in playlists['items']:
                    print(playlist['name'])
            return HttpResponse('/thanks/')
    else:
        form = usernameForm()
    return render(request, 'spotify/home.html', {'form': form})


    '''
    if request.method == 'POST':
        #print(cred.parameters)
        response = requests.get(cred.AUTH_URL, params=cred.parameters)
        print (response.text)
        return HttpResponse(response.content)
    '''
def callback(request):
    print("Made it into the callback function")
    return HttpResponse("Successfully made it back from the Spotify API")
