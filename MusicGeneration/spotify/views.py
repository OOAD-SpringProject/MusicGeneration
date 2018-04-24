import spotipy
import spotipy.util as util
from spotipy import oauth2
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
sp_oauth = oauth2.SpotifyOAuth( cred.CLIENT_ID, cred.CLIENT_SECRET, cred.REDIRECT_URI, scope=cred.SCOPE, cache_path=cred.CACHE )

def login(request):
    if request.method == 'POST':
        form = usernameForm(request.POST)
        if form.is_valid():
            userID = form.cleaned_data['userID']
            print(userID)
            token = util.prompt_for_user_token(userID, cred.SCOPE, client_id=cred.CLIENT_ID, client_secret=cred.CLIENT_SECRET, redirect_uri=cred.REDIRECT_URI)
            '''
            if token:
                sp = spotipy.Spotify(auth=token)
                playlists = sp.user_playlists(userID)
                for playlist in playlists['items']:
                    print(playlist['name'])
            return HttpResponse('/thanks/')
    else:
        form = usernameForm()
    return render(request, 'spotify/home.html', {'form': form})

    if request.method == 'POST':
        #print(cred.parameters)
        response = requests.get(cred.AUTH_URL, params=cred.parameters)
        print (response.text)
        return HttpResponse(response.content)
    '''

def callback(request):
    #print("Made it into the callback function")
    code = request.GET['code']
    if code:
        print ("Found code in URL, requesting access token...")
        gen_token = sp_oauth.get_access_token(code)
        access_token = gen_token['access_token']
        refresh_token = gen_token['refresh_token']

    if access_token and refresh_token:
        print("Successfully retrieved tokens")
    return HttpResponse("Access was granted!\n Currently gathering fresh tokens..." )
