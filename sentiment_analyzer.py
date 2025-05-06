from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from text_cleaner import clean_text
from emotion_mapper import emoji_map, emotion_map

def analyze_text(text):
    analyzer = SentimentIntensityAnalyzer()
    cleaned = clean_text(text)
    score = analyzer.polarity_scores(cleaned)
    compound = score['compound']

    if compound >= 0.05:
        sentiment = 'Positive'
        emotion = 'joy'
    elif compound <= -0.05:
        sentiment = 'Negative'
        emotion = 'anger'
    else:
        sentiment = 'Neutral'
        emotion = 'sadness'

    return {
        "Original Text": text,
        "Cleaned Text": cleaned,
        "Sentiment": sentiment,
        "Compound Score": compound,
        "Emoji": emoji_map[sentiment],
        "Emotion": emotion_map[emotion]
    }
