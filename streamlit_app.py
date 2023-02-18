# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
import streamlit as st
from pytube import YouTube, Search

# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
#     client_id='29b30746b4ca4a3b81c326357067bebd', client_secret='a49cb1c7277647499d115c13eac55a78'))

st.title('Spotify Song Downloader')

st.write('Enter the name of the song you want to download')

song_name = st.text_input('Song Name')

if st.button('Download'):
    search = Search(song_name)
    results = search.results[0].watch_url
    yt = YouTube(results).streams.get_by_itag(251).download()
    if not yt:
        st.write('Song not found')
    else:
        st.write('Song found')
        st.audio(yt)

        with yt.open('rb') as f:
            btn = st.download_button(label='Download', data=f,
                                     file_name=f'{song_name}.mp3', mime='audio/mp3')
