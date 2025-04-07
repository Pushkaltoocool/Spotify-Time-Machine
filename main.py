from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

year = input("Which year do you want to travel back to? Type the date in this format YYYY-MM-DD: ")

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}

response = requests.get(f"https://www.billboard.com/charts/hot-100/{year}", headers=header)

if response.status_code != 200:
    print("Failed to retrieve data. Check the date format or your internet connection.")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

songs = []
song_urls = []

song_tags = soup.select("li.o-chart-results-list__item h3#title-of-a-story")

for tag in song_tags:
    title = tag.get_text(strip=True)
    songs.append(title)

print(songs)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope='playlist-read-private playlist-modify-private playlist-modify-public user-library-read'
    ),
    requests_timeout=30
)

playlist = sp.user_playlist_create(user=sp.current_user()['id'], name=year, collaborative=False, description="test")
playlist_id = playlist['id']


for song in songs:
    result = sp.search(q=song, limit=1, type='track')
    try:
        track = result['tracks']['items'][0]
    except:
        song_urls.append(track["uri"])


sp.playlist_add_items(playlist_id=playlist_id, items=song_urls)

print("Created playlist titled : {year}, Added songs ✔")
