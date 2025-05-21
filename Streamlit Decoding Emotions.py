import streamlit as st
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Emoji Mapping for Sentiments
emoji_map = {
    "Positive": "😊",
    "Negative": "😠",
    "Neutral": "😐"
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

# Function to analyze sentiment
def analyze_text(text):
    cleaned = clean_text(text)
    score = analyzer.polarity_scores(cleaned)
    compound = score['compound']
    sentiment = "Positive" if compound >= 0.05 else "Negative" if compound <= -0.05 else "Neutral"
    emoji = emoji_map[sentiment]  # Get corresponding emoji
    return cleaned, sentiment, compound, emoji

# Streamlit UI
st.title("🔍 Social Media Sentiment & Emotion Analyzer 💬")

user_input = st.text_area("Enter your text here:", "")
if user_input:
    cleaned_text, sentiment, compound_score, emoji = analyze_text(user_input)
    st.write(f"**Cleaned Text:** {cleaned_text}")
    st.write(f"**Sentiment:** {sentiment} {emoji}")
    st.write(f"**Compound Score:** {compound_score}")

    # Pie Chart Visualization
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    sentiment_counts[sentiment] += 1  # Track sentiment distribution

    fig, ax = plt.subplots()
    ax.pie(sentiment_counts.values(), labels=sentiment_counts.keys(), autopct='%1.1f%%', colors=['green', 'red', 'blue'])
    plt.title("Sentiment Distribution")
    st.pyplot(fig)
    scores = pd.DataFrame({'Sentiment Score': [compound_score]})
    st.bar_chart(scores)
