from . import cred

class SpotifySession(object):
    def __init__(self, client_id="", secret_id="", refresh_token=""):
        self.client_id = client_id
        self.secret_id = secret_id
        self.refresh_token = refresh_token

    def setClientID(clientID):
        self.client_id = clientID

    def getClientID():
        return self.client_id

    def setRefreshToken(new_token):
        self.refresh_token = new_token

    def getRefreshToken():
        return self.refresh_token

class Song(object):
    def __init__(self, name="", genre="", artist=""):
        self.name = name
        self.genre = genre
        self.artist = artist

        def getName():
            return self.name
        def setName(new_name):
            self.name = new_name

        def getGenre():
            return self.genre
        def setGenre(new_genre):
            self.genre = new_genre

        def getArtist():
            return self.artist
        def setArtist(new_artist):
            self.artist = new_artist
