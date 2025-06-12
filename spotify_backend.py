import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Setup Spotipy with OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="user-read-private"
))

def get_track_features(track_name):
    results = sp.search(q=track_name, type='track', limit=1)
    if not results['tracks']['items']:
        return None
    track = results['tracks']['items'][0]
    features = sp.audio_features([track['id']])[0]
    return features, track['name'], track['artists'][0]['name'], track['external_urls']['spotify']
