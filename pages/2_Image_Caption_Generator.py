import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

st.set_page_config(page_title="🖼️ Batch Image Caption Generator", layout="centered")
st.title("🖼️ Batch AI Image Caption Generator (Up to 4 Images)")

st.markdown("""
Upload multiple images (max 4) and get AI-generated captions for each.  
Powered by **BLIP** (Bootstrapped Language Image Pretraining).
""")

# Load BLIP model (cached)
@st.cache_resource
def load_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

processor, model = load_model()

# Upload multiple images
uploaded_files = st.file_uploader("Upload up to 4 images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

# Limit file count
if uploaded_files and len(uploaded_files) > 4:
    st.warning("Please upload no more than 4 images.")
    uploaded_files = uploaded_files[:4]

# Generate captions
if uploaded_files and st.button("🧠 Generate Captions"):
    for i, file in enumerate(uploaded_files):
        st.markdown(f"### 🖼️ Image {i + 1}")
        image = Image.open(file).convert('RGB')
        st.image(image, use_container_width=True)

        with st.spinner("Generating caption..."):
            inputs = processor(images=image, return_tensors="pt")
            out = model.generate(**inputs)
            caption = processor.decode(out[0], skip_special_tokens=True)

        st.success(f"📝 Caption: **{caption}**")
        st.markdown("---")