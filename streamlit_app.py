import streamlit as st
from pytube import YouTube, Search

st.title("Song Downloader")
st.write("Enter the name of the song you want to download")
song_name = st.text_input("Song Name")
if st.button:
    st.write("Searching for the song")
    search = Search(song_name)
    st.write("Song Found")
    st.write("Downloading the song")
    search.results[0].streams.first().download()
    st.write("Song Downloaded")
