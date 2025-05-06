import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

st.set_page_config(page_title="🧠 Sentiment Analyzer", layout="centered")
st.title("🧠 News & Text Sentiment Analyzer")

st.markdown("""
Analyze the **emotional tone** of any news snippet, tweet, or short message.  
This tool predicts whether your text expresses a **Positive**, **Neutral**, or **Negative** sentiment.

Model: `cardiffnlp/twitter-roberta-base-sentiment`
""")

# Load model & tokenizer (cached)
@st.cache_resource
def load_model():
    model_name = "cardiffnlp/twitter-roberta-base-sentiment"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_model()

# Emoji mapping for output
emoji_map = {
    "Positive": "🟢",
    "Neutral": "⚪",
    "Negative": "🔴"
}

# User input
text = st.text_area("📝 Paste a headline, tweet, or short text:", height=150)

if st.button("🔍 Analyze Sentiment"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Analyzing sentiment..."):
            inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
            outputs = model(**inputs)
            probs = F.softmax(outputs.logits, dim=1).squeeze()
            labels = ['Negative', 'Neutral', 'Positive']
            prediction = torch.argmax(probs).item()
            confidence = probs[prediction].item()

        sentiment = labels[prediction]
        emoji = emoji_map[sentiment]

        st.markdown(f"### {emoji} Sentiment: **{sentiment}**")
        st.write(f"🧠 Confidence: `{confidence * 100:.2f}%`")

