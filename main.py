import streamlit as st
from spotify_backend import get_track_features

st.set_page_config(page_title="Music Recommender", page_icon="🎵")
st.title("🎵 Free Music Recommender")
st.markdown("Enter a song you like, and we'll suggest similar tracks based on audio features!")

track_name = st.text_input("🎧 Enter a song title")

if st.button("Recommend"):
    data = get_track_features(track_name)
    if data:
        st.success(f"**{data['name']}** by *{data['artist']}*")
        st.markdown(f"[Listen on Spotify]({data['url']})")
        st.info("🎯 Recommendations coming soon...")
    else:
        st.error("❌ Song not found. Try a different title.")
