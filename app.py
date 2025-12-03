import streamlit as st
import json
import random

# ----------------------------
# PAGE TITLE
# ----------------------------
st.set_page_config(page_title="MiniFlix Chatbot", page_icon="🎬")
st.title("🎬 MiniFlix Bollywood Chatbot")
st.write("Get movie suggestions based on mood or genre!")

# ----------------------------
# LOAD MOVIES DATA
# ----------------------------
with open("movies.json", "r", encoding="utf-8") as f:
    movies = json.load(f)

# ----------------------------
# HELPER FUNCTIONS
# ----------------------------
def get_movies_by_genre(genre):
    genre = genre.lower()
    return [m for m in movies if genre in [g.lower() for g in m["genre"]]]

def get_movies_by_mood(mood):
    mood = mood.lower()
    return [m for m in movies if mood in [md.lower() for md in m["mood"]]]

# ----------------------------
# USER INPUT
# ----------------------------
user_msg = st.text_input("What do you feel like watching? (romantic, horror, comedy…)")

# ----------------------------
# SURPRISE ME FEATURE
# ----------------------------
if st.button("🎁 Surprise Me"):
    movie = random.choice(movies)
    st.subheader("✨ Surprise Pick!")
    st.image(movie["poster"])
    st.write(f"### {movie['title']}")
    st.write(movie["description"])
    st.write("**Genre:** " + ", ".join(movie["genre"]))
    st.write("**Mood:** " + ", ".join(movie["mood"]))

# ----------------------------
# KEYWORD MAPS FOR CHATBOT
# ----------------------------
genre_map = {
    "romance": ["romance", "love", "romantic"],
    "comedy": ["comedy", "funny", "laugh"],
    "horror": ["horror", "ghost", "scary", "spooky"],
    "thriller": ["thriller", "suspense"],
    "action": ["action", "fight"],
    "drama": ["drama", "serious"],
    "family": ["family"],
    "adventure": ["adventure", "travel"],
    "musical": ["musical", "music"],
    "sports": ["sports"],
    "biography": ["biography", "biopic"],
    "crime": ["crime", "murder"],
    "war": ["war"],
    "history": ["history", "historical"],
    "patriotic": ["patriotic"],
    "mystery": ["mystery"]
}

mood_map = {
    "feel-good": ["feel good", "happy"],
    "emotional": ["emotional", "cry"],
    "dark": ["dark", "intense"],
    "youth": ["youth", "young"],
    "travel": ["road trip", "travel"]
}

# ----------------------------
# CHATBOT LOGIC
# ----------------------------
if user_msg:
    msg = user_msg.lower()
    matched_genre = None
    matched_mood = None

    # Check genre match
    for genre, keywords in genre_map.items():
        if any(k in msg for k in keywords):
            matched_genre = genre
            break

    # Check mood match
    for mood, keywords in mood_map.items():
        if any(k in msg for k in keywords):
            matched_mood = mood
            break

    # Show results
    results = []

    if matched_genre:
        st.subheader(f"🎬 {matched_genre.title()} Movies")
        results = get_movies_by_genre(matched_genre)

    elif matched_mood:
        st.subheader(f"💫 {matched_mood.title()} Picks")
        results = get_movies_by_mood(matched_mood)

    else:
        st.write("Sorry, I didn’t understand. Try keywords like:")
        st.write("romantic, horror, comedy, emotional, feel good, youth, crime, travel")
    
    # Display movies
    for movie in results[:4]:
        st.write("### " + movie["title"])
        st.image(movie["poster"])
        st.write(movie["description"])
        st.write("Genre: " + ", ".join(movie["genre"]))
        st.write("Mood: " + ", ".join(movie["mood"]))
        st.write("---")

