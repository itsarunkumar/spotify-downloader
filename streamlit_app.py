import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pytube import Search, YouTube, Playlist
from moviepy import editor as mp

st.title("Spotify Downloader")

st.write("This is a simple Spotify Downloader")

url = st.text_input("Enter Spotify Playlist URL")

if st.button("Download"):
    playlist_url = url
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
        client_id='29b30746b4ca4a3b81c326357067bebd', client_secret='a49cb1c7277647499d115c13eac55a78'))
    results = spotify.playlist(playlist_url)
    for idx, item in enumerate(results['tracks']['items']):
        track = item['track']
        st.write(idx, track['artists'][0]['name'], " – ", track['name'])
        search = Search(track['artists'][0]['name'] + " – " + track['name'])
        yt = YouTube(
            search.results[0].watch_url).streams.get_highest_resolution()
        download_file = yt.download()
        clip = mp.VideoFileClip(download_file)
        audio = clip.audio.write_audiofile(
            track['artists'][0]['name'] + " – " + track['name'] + ".mp3")
        st.write("Downloaded: " + track['artists']
                 [0]['name'] + " – " + track['name'])
