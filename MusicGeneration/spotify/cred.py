# Spotify ID codes. Needs to be kept secret
CLIENT_ID = "7b58acd087c64768bcbc2c333bdae67c"
CLIENT_SECRET = "546b09f9105e4e60813e6b016b4a1665"

# Spotify API URLs
API_URL = "https://api.spoitfy.com/v1"
AUTH_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"

# Extra info needed for API requests
REDIRECT_URI = "http://127.0.0.1:8000/callback"
SCOPE = "playlist-read-private playlist-modify-public playlist-modify-private"

parameters = {
    "client_id": CLIENT_ID,
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    "scope": SCOPE
}
