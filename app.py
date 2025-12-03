import streamlit as st
import json
import random

# Page settings
st.set_page_config(page_title="MiniFlix Chatbot", page_icon="🎬", layout="centered")

# Load dataset
with open("movies.json", "r") as f:
    movies = json.load(f)

# App title
st.title("🎬 MiniFlix Chatbot")
st.write("Hey! Ask me for movie suggestions based on mood, genre, or vibe ✨")

# User input
user_msg = st.text_input("Type something like 'suggest a romantic movie' or 'thriller please'")

# Helper function
def get_movies_by_genre(g):
    return [m for m in movies if g in m["genre"]]

def get_movies_by_mood(m):
    return [mov for mov in movies if m in mov["mood"]]

# Surprise button
if st.button("🎁 Surprise Me!"):
    movie = random.choice(movies)
    st.subheader("✨ Your Surprise Pick")
    st.image(movie["poster"], width=200)
    st.write(f"**{movie['title']}**")
    st.write(movie["description"])

# Chat logic
if user_msg:
    msg = user_msg.lower()

    # Mood-based
    if any(word in msg for word in ["romantic", "love"]):
        recs = get_movies_by_genre("romance")
        st.subheader("💌 Romantic Picks")
    elif any(word in msg for word in ["funny", "comedy"]):
        recs = get_movies_by_mood("feel-good")
        st.subheader("😂 Comedy / Feel-good Picks")
    elif "thriller" in msg:
        recs = get_movies_by_genre("thriller")
        st.subheader("🖤 Thriller Picks")
    elif "dark" in msg:
        recs = get_movies_by_mood("dark")
        st.subheader("🌑 Dark Vibe Picks")
    else:
        st.write("Not sure about that vibe 😅 Try: romantic, funny, thriller, dark")
        recs = []

    # Display recommendations
    for r in recs[:3]:
        with st.container():
            st.image(r["poster"], width=200)
            st.write(f"**{r['title']}**")
            st.write(r["description"])
