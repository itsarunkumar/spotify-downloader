import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import streamlit as st
import pandas as pd
import numpy as np
from pytube import YouTube, Search

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id='29b30746b4ca4a3b81c326357067bebd', client_secret='a49cb1c7277647499d115c13eac55a78'))

st.title('Spotify Song Downloader')

st.write('Enter the name of the song you want to download')

song_name = st.text_input('Song Name')

if st.button('Download'):
    results = spotify.search(q='track:' + song_name, type='track')
    for idx, track in enumerate(results['tracks']['items']):
        track_name = st.write(idx, track['name'])
        st.write(track['artists'][0]['name'])
        st.write(track['external_urls']['spotify'])

        search = Search(song_name)
        url = search.results[0].watch_url
        yt = YouTube(url).streams.get_audio_only()
        yt_downlaoded = yt.download()

        st.write('Downloaded' + song_name + 'successfully')

        st.download_button('Download', yt_downlaoded, 'mp3')
