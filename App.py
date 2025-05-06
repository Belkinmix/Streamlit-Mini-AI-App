import streamlit as st
from PIL import Image

st.set_page_config(page_title="AI Assistant", page_icon="🤖", layout="centered")

image = Image.open("assets/robot_intro.png")
st.image(image, use_container_width=True)

st.title("🧬🧠🖥️ AI Playground - A Small AI App")

# Intro
st.markdown("""
Welcome to my small AI app – a showcase of interactive AI-powered applications built with Streamlit!

This project brings together real-time **emotion detection** from images or webcam feed, **image caption generation** capabilities, as well as **sentiment analysis**, demonstrating how modern AI models can be integrated into intuitive web applications.

### Features Included:
- **Emotion Detection** from your image or webcam feed
- **Image Caption Generator** powered by BLIP
- **Multilingual Text Assistant** with FLAN-T5 by Google
- **Sentiment Analyzer** for headlines, tweets, or articles
- **Fun Zone** full of surprises: emojis, fireworks, music, easter eggs!

---

### Technologies Used:
- Python, Streamlit & Anaconda
- DeepFace for facial analysis
- Hugging Face Transformers: `blip`, `flan-t5`, `roberta-sentiment`
- Torch, PIL, WebRTC
- Fun extras: `streamlit-extras`, emojis, MP3 playback, and more!

❗🚨 **Note**:  
Some models (especially image- or text-based ones) may take a few seconds (or a bit more) to load the first time you use them.  
Please be patient — they're worth the wait! :)

---

### Navigation:
Use the **sidebar** to explore all features:
- Emotion Detection
- Image Captioning
- AI Text Assistant
- Sentiment Analyzer
- The Fun Zone (yes, it got crazier), use the word "banana" for a surpise!


---
If you like this project, feel free to connect with me!  
**GitHub:** [https://github.com/Belkinmix]  
**LinkedIn:** [https://www.linkedin.com/in/belkinmikhail/]

Happy exploring!
""")