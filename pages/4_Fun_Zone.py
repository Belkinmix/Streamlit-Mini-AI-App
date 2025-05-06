import streamlit as st
import time
from streamlit_extras.let_it_rain import rain
import random

st.title("🏠 Welcome to the Fun Zone :D")
st.markdown("This is the page with some fun!")

st.subheader("🔴 Mystery Button")
if st.button("Press me :D"):
    st.toast('Look ! It is a cool message !', icon='😎')
    time.sleep(1.5)
    st.toast('Another cool message !', icon='😎')
    time.sleep(1.5)
    st.toast('Look ! Balloons !', icon='🎈')
    st.balloons()

st.subheader("🔴 Another Mystery Button")
if st.button("Make it rain"):
    rain(emoji="🎈", 
         font_size=54, 
         falling_speed=5, 
         animation_length="1")

# --- Celebration Music 🎵 ---
st.subheader("🎵 Random Celebration Music")
if st.button("🔊 Play Random Track"):
    songs = [
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"
    ]
    song_choice = random.choice(songs)
    st.audio(song_choice)


# --- 🥚 Secret Easter Egg ---
st.subheader("🥚 Secret Easter Egg")
code = st.text_input("Enter the magic word...")
st.subheader("A small hint - you have probably seen it on the 'App' page")

if code.lower().strip() == "banana":
    st.markdown("### 🍌 You unlocked... **TOTAL MADNESS** 🎉💥🔥")
    rain(emoji="🔥", font_size=48, falling_speed=10, animation_length="2")
    rain(emoji="🌈", font_size=48, falling_speed=5, animation_length="2")
    st.toast("🔥 You crazy genius 🔥", icon="💡")
    st.balloons()
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3")