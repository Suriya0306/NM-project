import streamlit as st
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

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
    return cleaned, sentiment, compound

# Streamlit UI
st.title("Social Media Sentiment & Emotion Analyzer")

user_input = st.text_area("Enter your text here:", "")
if user_input:
    cleaned_text, sentiment, compound_score = analyze_text(user_input)
    st.write(f"**Cleaned Text:** {cleaned_text}")
    st.write(f"**Sentiment:** {sentiment}")
    st.write(f"**Compound Score:** {compound_score}")

    # Visualization
    scores = pd.DataFrame({'Sentiment Score': [compound_score]})
    st.bar_chart(scores)
