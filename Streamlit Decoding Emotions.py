import streamlit as st
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Sentiment & Emotion Mapping
emoji_map = {
    "Positive": "😊",
    "Negative": "😠",
    "Neutral": "😐"
}

emotion_map = {
    "joy": "😊",
    "sadness": "😢",
    "anger": "😠",
    "fear": "😨",
    "surprise": "😮"
}

# Initialize Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to clean text
def clean_text(text):
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
    text = re.sub(r'@\w+|#\w+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower().strip()
    return text

# Function to analyze sentiment and emotion
def analyze_text(text):
    cleaned = clean_text(text)
    score = analyzer.polarity_scores(cleaned)
    compound = score['compound']
    
    # Determine Sentiment
    if compound >= 0.05:
        sentiment = "Positive"
        emotion = "joy"
    elif compound <= -0.05:
        sentiment = "Negative"
        emotion = "anger"
    else:
        sentiment = "Neutral"
        emotion = "sadness"
    
    return cleaned, sentiment, compound, emotion

# Streamlit UI
st.title("🔍 Social Media Sentiment & Emotion Analyzer 💬")

user_input = st.text_area("Enter your text here:", "")
if user_input:
    cleaned_text, sentiment, compound_score, emotion = analyze_text(user_input)
    st.write(f"**Cleaned Text:** {cleaned_text}")
    st.write(f"**Sentiment:** {sentiment} {emoji_map[sentiment]}")
    st.write(f"**Emotion:** {emotion.capitalize()} {emotion_map[emotion]}")
    st.write(f"**Compound Score:** {compound_score}")

    # Sentiment Distribution Visualization
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    sentiment_counts[sentiment] += 1

    fig, ax = plt.subplots()
    ax.pie(sentiment_counts.values(), labels=sentiment_counts.keys(), autopct='%1.1f%%', colors=['green', 'red', 'blue'])
    plt.title("Sentiment Distribution")
    st.pyplot(fig)
