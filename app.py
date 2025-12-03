import streamlit as st
import json
import random


st.set_page_config(page_title="MiniFlix Chatbot", page_icon="🎬", layout="wide")

st.markdown("""
<style>

body {
    background-color: #111;
    color: white;
}

.movie-card {
    background: rgba(255, 255, 255, 0.06);
    padding: 20px;
    border-radius: 12px;
    backdrop-filter: blur(5px);
    color: white;
    border: 1px solid rgba(255,255,255,0.1);
}

input {
    background-color: white !important;
}

</style>
""", unsafe_allow_html=True)


with open("movies.json", "r", encoding="utf-8") as f:
    movies = json.load(f)


st.markdown("""
<div style="text-align:center; padding:20px;">
    <h1 style="color:#E50914; font-size:50px; margin-bottom:5px;">🎬 MiniFlix Chatbot</h1>
    <p style="font-size:20px; color:#ccc;">Your Bollywood recommendation assistant ✨</p>
</div>
""", unsafe_allow_html=True)


user_msg = st.text_input("💬 What do you feel like watching? (romantic, horror, comedy, etc.)", "")


def get_movies_by_genre(genre):
    return [m for m in movies if genre.lower() in [g.lower() for g in m["genre"]]]

def get_movies_by_mood(mood):
    return [m for m in movies if mood.lower() in [md.lower() for md in m["mood"]]]

# --------------------------------------------
# SURPRISE ME BUTTON
# --------------------------------------------
if st.button("🎁 Surprise Me"):
    movie = random.choice(movies)
    st.subheader("✨ Your Surprise Pick!")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(movie["poster"], use_column_width=True)
    with col2:
        st.markdown(
            f"""
            <div class="movie-card">
                <h2>{movie['title']}</h2>
                <p>{movie['description']}</p>
                <p><b>Genre:</b> {", ".join(movie["genre"]).title()}</p>
                <p><b>Mood:</b> {", ".join(movie["mood"]).title()}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# --------------------------------------------
# SMART CHAT LOGIC
# --------------------------------------------
if user_msg:
    msg = user_msg.lower()
    recs = []

    genre_map = {
        "romance": ["romance", "love", "romantic"],
        "comedy": ["comedy", "funny", "laugh"],
        "horror": ["horror", "ghost", "scary", "spooky"],
        "thriller": ["thriller", "suspense", "edge", "tension"],
        "action": ["action", "fight", "hero"],
        "drama": ["drama", "serious"],
        "family": ["family"],
        "adventure": ["adventure", "travel"],
        "musical": ["musical", "music"],
        "sports": ["sports"],
        "biography": ["biography", "biopic"],
        "crime": ["crime", "murder"],
        "war": ["war"],
        "history": ["history", "historical"],
        "patriotic": ["patriotic", "nation"],
        "mystery": ["mystery"]
    }

    mood_map = {
        "feel-good": ["feel good", "happy", "uplifting"],
        "emotional": ["emotional", "cry", "tears"],
        "dark": ["dark", "intense"],
        "youth": ["youth", "young", "college"],
        "travel": ["road trip", "travel", "trip"]
    }

    matched_genre = None
    for genre, keywords in genre_map.items():
        if any(k in msg for k in keywords):
            matched_genre = genre
            break

    matched_mood = None
    for mood, keywords in mood_map.items():
        if any(k in msg for k in keywords):
            matched_mood = mood
            break

    if matched_genre:
        recs = get_movies_by_genre(matched_genre)
        st.subheader(f"🎬 {matched_genre.title()} Movies For You")

    elif matched_mood:
        recs = get_movies_by_mood(matched_mood)
        st.subheader(f"💫 {matched_mood.title()} Picks")

    else:
        st.subheader("🤔 Try searching for:")
        st.write("romance, comedy, horror, thriller, emotional, feel-good, youth, patriotic, crime")
        recs = []

    # --------------------------------------------
    # MOVIE CARD DISPLAY
    # --------------------------------------------
    for r in recs[:6]:
        st.markdown("---")
        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(r["poster"], use_column_width=True)

        with col2:
            st.markdown(
                f"""
                <div class="movie-card">
                    <h2>{r['title']}</h2>
                    <p>{r['description']}</p>
                    <p><b>Genre:</b> {", ".join(r["genre"]).title()}</p>
                    <p><b>Mood:</b> {", ".join(r["mood"]).title()}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
