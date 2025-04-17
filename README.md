# 🎵 Spotify Time Machine

Travel back in time and relive the top hits of your favorite date!  
This Python script scrapes the Billboard Hot 100 chart for any past date and automatically creates a Spotify playlist with those songs.

## 🛠️ Features

- 📅 Choose any date from the past
- 🎶 Automatically find songs from Billboard Hot 100
- 🔗 Create a Spotify playlist with a single script
- 🔐 Authenticates securely with Spotify API

## 🚀 How It Works

1. Input a date like `2005-08-14`
2. Script scrapes [Billboard Hot 100](https://www.billboard.com/charts/hot-100/)
3. Spotify API is used to:
   - Search for each song
   - Create a new playlist
   - Add all available songs to your account

## 📦 Technologies

- Python
- BeautifulSoup (Web scraping)
- Spotipy (Spotify API wrapper)
- dotenv (.env config)
