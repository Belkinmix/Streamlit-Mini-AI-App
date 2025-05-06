import streamlit as st
from deepface import DeepFace
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import numpy as np
import cv2
from PIL import Image

st.title("😊 Emotion Detection")

option = st.radio("Choose Input Method:", ["📷 Use Webcam", "🖼️ Upload Image"])

class EmotionDetector(VideoTransformerBase):
    def __init__(self):
        self.frame = None

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        self.frame = img.copy()
        return img

if option == "📷 Use Webcam":
    ctx = webrtc_streamer(key="webcam", video_transformer_factory=EmotionDetector)
    if ctx.video_transformer:
        if st.button("📸 Capture and Analyze"):
            frame = ctx.video_transformer.frame
            if frame is not None:
                st.image(frame, channels="BGR")
                with st.spinner("Analyzing..."):
                    result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                    emotion = result[0]["dominant_emotion"]
                    st.success(f"Emotion: **{emotion.capitalize()}**")
                    scores = {k: f"{v:.2f}%" for k, v in result[0]["emotion"].items()}
                    st.table(scores)
else:
    file = st.file_uploader("Upload image", type=["jpg", "jpeg", "png"])
    if file:
        image = Image.open(file).convert("RGB")
        img_array = np.array(image)
        st.image(img_array)
        if st.button("🔍 Analyze"):
            result = DeepFace.analyze(img_array, actions=['emotion'], enforce_detection=False)
            emotion = result[0]["dominant_emotion"]
            st.success(f"Emotion: **{emotion.capitalize()}**")
            scores = {k: f"{v:.2f}%" for k, v in result[0]["emotion"].items()}
            st.table(scores)