from sentiment_analyzer import analyze_text
from visualizer import plot_sentiment_distribution

print("Welcome to the Social Media Sentiment and Emotion Analyzer!")
user_texts = []

while True:
    entry = input("Enter text (type 'done' to finish): ")
    if entry.lower() == "done":
        break
    user_texts.append(entry)

if user_texts:
    results = [analyze_text(text) for text in user_texts]

    for result in results:
        print(result)

    # Collect sentiment counts
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    for res in results:
        sentiment_counts[res["Sentiment"]] += 1

    plot_sentiment_distribution(sentiment_counts)

print("Thank you for using the Sentiment and Emotion Analyzer. Goodbye!")
