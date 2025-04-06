# main.py (excerpt)
import nltk
nltk.download('vader_lexicon')

from data_fetch import fetch_wikipedia_text
from processing import clean_text, get_word_frequencies, get_summary_stats, analyze_sentiment

if __name__ == "__main__":
    raw_text = fetch_wikipedia_text("To_Kill_a_Mockingbird")
    cleaned = clean_text(raw_text)
    freq_counter = get_word_frequencies(cleaned)
    top20 = freq_counter.most_common(20)
    total, unique, avg_len = get_summary_stats(cleaned.split())
    sentiment_scores = analyze_sentiment(raw_text)
    
    # Print or save results
    print("Top 20 words:", top20)
    print(f"Total words: {total}, Unique words: {unique}, Avg. word length: {avg_len:.2f}")
    print("Sentiment (VADER):", sentiment_scores)
