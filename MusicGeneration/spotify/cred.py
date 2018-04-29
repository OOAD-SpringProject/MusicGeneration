from requests.utils import quote


# Spotify ID codes
CLIENT_ID = "3d91540b00614c47a8699c099f3083ab"
CLIENT_SECRET = "b79741704420459ea891007c04faac77"

# Spotify API URLs
API_URL = "https://api.spoitfy.com/v1"
AUTH_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"

# Extra info needed for API requests
REDIRECT_URI = "http://127.0.0.1:8000/callback"
#SCOPE = "playlist-read-private playlist-modify playlist-modify-private"
SCOPE = "playlist-read-private playlist-modify public"

parameters = {
    "client_id": CLIENT_ID,
    "response_type": "code",
    "redirect_uri": quote(REDIRECT_URI, safe=''),
    "scope": quote(SCOPE, safe='')
}

CACHE = '.spotipyoauthcache'
