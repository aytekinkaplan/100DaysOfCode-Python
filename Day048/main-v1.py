import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests
from datetime import datetime

# Spotify API kimlik bilgileri
SPOTIFY_CLIENT_ID = "YOUR_CLIENT_ID"
SPOTIFY_CLIENT_SECRET = "YOUR_CLIENT_SECRET"
SPOTIFY_REDIRECT_URI = "http://example.com"  # Bu, Spotify Developer Dashboard'da ayarladığınız URI olmalı

# Tarih girişi
while True:
    date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    try:
        datetime.strptime(date, '%Y-%m-%d')
        break
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

# Billboard verilerini çek
URL = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.select("li ul li h3.c-title")
song_names = [song.getText().strip() for song in song_names_spans]

# Spotify yetkilendirme
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIFY_REDIRECT_URI,
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

# Şarkıları Spotify'da ara ve URI'lerini kaydet
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Yeni çalma listesi oluştur
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

# Şarkıları çalma listesine ekle
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

print(f"Playlist '{date} Billboard 100' created successfully on Spotify!")