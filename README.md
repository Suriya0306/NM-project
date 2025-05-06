# NM-project
# Social Media Sentiment & Emotion Analyzer
A Python-based tool that analyzes social media text, detects sentiments (Positive, Negative, Neutral) and emotions (Joy, Sadness, Anger, Fear, Surprise), and visualizes results using pie charts.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Example Output](#example-output)
- [Contributions](#contributions)
- [License](#license)

## Overview
This project leverages VADER Sentiment Analysis to detect the emotional tone of text input from social media posts. It categorizes sentiments into Positive, Negative, and Neutral, while also identifying emotions such as:

Joy 😊
Sadness 😢
Anger 😠
Fear 😨
Surprise
## Features
✅ Sentiment analysis using VADER 
✅ Emotion classification with emoji mapping 
✅ Text preprocessing to remove noise 
✅ Pie charts for sentiment and emotion visualization 
✅ CSV file storage for analysis

## Technologies
Python – Programming language
VADER Sentiment Analysis – NLP-based sentiment detection
Pandas – Data manipulation
Matplotlib – Graphical visualization
Regular Expressions (re) – Text cleaning
Installation
To install dependencies, run: "pip install pandas matplotlib vaderSentiment"

## Usage
Run the script and input social media texts for analysis: python sentiment_analyzer.py

## Example Output
Sentiment Breakdown: Positive: 45.00% 😊 Negative: 30.00% 😠 Neutral: 25.00% 😐

Emotional Breakdown: Joy: 50.00% 😊 Sadness: 20.00% 😢 Anger: 30.00% 😠 Visualization charts are displayed for sentiment and emotion distribution.

## Contributions
Feel free to fork and contribute to improve the accuracy or visualization.

## License
This project is licensed under the MIT License.
