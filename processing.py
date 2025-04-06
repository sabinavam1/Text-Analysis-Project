# processing.py (excerpt)
import re
from collections import Counter
# Optional: NLTK's VADER for sentiment
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Clean text: remove punctuation and make lowercase
def clean_text(text):
    text = re.sub(r"[^A-Za-z0-9 ]+", " ", text)  # keep letters/numbers, replace others with space
    return text.lower()

# Get word frequency (excluding stop words)
STOP_WORDS = set([...])  # (common English stop words list)
def get_word_frequencies(text):
    words = [w for w in text.split() if w not in STOP_WORDS]
    return Counter(words)

# Summary statistics: total words, unique words, average length
def get_summary_stats(words_list):
    total = len(words_list)
    unique = len(set(words_list))
    avg_len = sum(len(w) for w in words_list) / total if total else 0
    return total, unique, avg_len

# Sentiment analysis using VADER
def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(text)
    return scores  # dict with 'pos', 'neu', 'neg', 'compound'
