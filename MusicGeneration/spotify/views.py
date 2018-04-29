import spotipy
import spotipy.util as util
from spotipy import oauth2
import random
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, Template
from . import cred
from .classes import usernameForm
import requests



# Create your views here.
def homePage(request):
    #body_content = {'needs_to_login': True, 'custom_message': "Variable is currently true"}
    #return render(request, 'spotify/home.html', body_content)
    return render(request, 'spotify/home.html')


def instruction(request):
    return render(request, 'spotify/instruction.html')


# Handling Spotify authorization here
sp_oauth = oauth2.SpotifyOAuth( cred.CLIENT_ID, cred.CLIENT_SECRET, cred.REDIRECT_URI, scope=cred.SCOPE, cache_path=cred.CACHE )
g_access_token = "holder"

def login(request):
    if request.method == 'POST':
        form = usernameForm(request.POST)
        if form.is_valid():
            userID = form.cleaned_data['userID']
            print(userID)
            token = util.prompt_for_user_token(userID, cred.SCOPE, client_id=cred.CLIENT_ID, client_secret=cred.CLIENT_SECRET, redirect_uri=cred.REDIRECT_URI)


def callback(request):
    #print("Made it into the callback function")
    code = str(request.GET['code'])
    if code:
        global g_access_token
        #main_code = code
        print ("Found code in URL, requesting access token...")
        gen_token = sp_oauth.get_access_token(code)
        access_token = gen_token['access_token']
        refresh_token = gen_token['refresh_token']

    if access_token and refresh_token:
        g_access_token = access_token
        print("Successfully retrieved tokens")
        sp = spotipy.Spotify(access_token)
        results = sp.current_user()
        name = results['display_name']
        user_id = results['id']
        playlists = sp.user_playlists(user_id)
        some_name = playlists['items']

        class ReturnInfo(object):
            def __init__(self, name, pl_id):
                self.name = name
                self.id = pl_id

        all_playlist_items = []
        for item in some_name:
            new_info = ReturnInfo(item['name'], item['name'])
            all_playlist_items.append(new_info)
        print (all_playlist_items)
        body_content = {'users_name': name, 'playlist_names': all_playlist_items}
        #print(sp.current_user())
    return render(request, 'spotify/instruction.html', body_content)

def result(request):
    if request.method == 'POST':
        selection_criteria = request.POST.getlist('select_criteria')
        playlist_selection_pre = request.POST.getlist('playlist_selection')
        playlist_selection = playlist_selection_pre[0]
    if g_access_token:
        print("Successfully retrieved token for the result")
        sp_g = spotipy.Spotify(g_access_token)
        results_g = sp_g.current_user()
        name_g = results_g['display_name']
        user_id_g = results_g['id']
        playlists = sp_g.user_playlists(user_id_g)
        some_name_g = playlists['items']
        playlist_id_g = []
        for item in some_name_g:
            if (item['name'] == playlist_selection):
                playlist_id_g.append(item['id'])
        sp_playlist = sp_g.user_playlist_tracks(user_id_g, playlist_id=playlist_id_g[0])
        tracks = sp_playlist['items']
        for item in tracks:
            more_info = item['track']['album']
            release_year = more_info['release_date']
        # Getting info to follow this playlist
        if release_year:
            search_result = sp_g.search(release_year, limit=1, offset=0, type='playlist')
            search_items = search_result['playlists']['items'][0]
            playlist_id_to_add = search_items['id']
            owner_id_to_add = search_items['owner']['id']
        # Make the user follow the playlist
        if playlist_id_to_add and owner_id_to_add:
            sp_g.user_playlist_follow_playlist(owner_id_to_add, playlist_id_to_add)

    return render(request, 'spotify/result.html')
