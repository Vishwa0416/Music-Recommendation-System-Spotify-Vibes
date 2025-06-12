import os
import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET
))

def get_track_features(track_name):
    results = sp.search(q=track_name, type='track', limit=1)
    if not results['tracks']['items']:
        return None, None, None, None
    track = results['tracks']['items'][0]
    features = sp.audio_features(track['id'])[0]
    return features, track['name'], track['artists'][0]['name'], track['external_urls']['spotify']

def recommend_similar_tracks(input_track, track_db):
    input_features, name, artist, url = get_track_features(input_track)
    if not input_features:
        return []

    df = pd.read_csv(track_db)

    feature_cols = ['danceability', 'energy', 'loudness', 'speechiness',
                    'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
    
    df_scaled = df.copy()
    scaler = MinMaxScaler()
    df_scaled[feature_cols] = scaler.fit_transform(df[feature_cols])
    
    input_vector = scaler.transform([[
        input_features[col] for col in feature_cols
    ]])

    similarities = cosine_similarity(input_vector, df_scaled[feature_cols])[0]
    df['similarity'] = similarities
    recommendations = df.sort_values(by='similarity', ascending=False).head(5)

    return recommendations[['name', 'artists', 'url', 'similarity']].to_dict(orient='records')
