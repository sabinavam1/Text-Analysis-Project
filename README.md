**1. Project Overview**  
In this project, I analyzed the Wikipedia article for *To Kill a Mockingbird* using Python. I accessed the article programmatically through the MediaWiki API and extracted its plain text content. I applied various computational text analysis techniques, including word frequency analysis, summary statistics (such as word count and average word length), and sentiment analysis using NLTK’s VADER tool. The goal was to understand the tone, language, and structure of the article while learning to use new tools, experimenting with APIs, and applying natural language processing.

**2. Implementation**  
The project is organized into three Python files:  
- `data_fetch.py` handles retrieving the Wikipedia text using the `urllib` and `JSON` modules.  
- `processing.py` includes helper functions for text cleaning, word frequency analysis, summary statistics, and sentiment analysis using NLTK.  
- `main.py` serves as the entry point. It calls functions from the other two modules and prints the final output.  

I utilized dictionaries (via `collections.Counter`) for frequency analysis and lists for handling words. The sentiment analysis employed NLTK's VADER tool to generate scores. Initially, I tried using the `requests` module but encountered environment issues, so I switched to `urllib.request` after troubleshooting with GenAI.

GenAI tools were instrumental throughout the project, helping with debugging import errors, downloading NLTK resources, and cleaning the text with regular expressions. I also used GenAI for assistance with error messages and to write some helper functions when necessary.

**3. Results**  
The top 20 words (prior to removing stop words) included common English terms such as "the," "and," and "of," as well as article-specific words like "Lee," "Scout," "Mockingbird," "novel," and "Atticus."  
**Summary statistics:**  
- Total words: 10,091  
- Unique words: 2,648  
- Average word length: 4.78 characters  

Sentiment analysis using VADER showed:  
`{'neg': 0.127, 'neu': 0.754, 'pos': 0.119, 'compound': -0.9996}`  
This reflects a mostly neutral tone with a slight negative skew, likely due to the article’s serious themes (e.g., racism, injustice). This project demonstrated that even Wikipedia articles, while written neutrally, can carry sentiment weight depending on the subject matter.

**4. Reflection**  
**What went well:** Once I successfully retrieved the data from Wikipedia, the modular code structure made testing and debugging easier. Breaking the project into separate files proved very helpful.  

**Biggest challenge:** I faced difficulties managing missing packages and environment issues, such as ImportError: No module named 'requests' and downloading NLTK data (specifically `vader_lexicon`). I resolved these issues with guidance from ChatGPT and relevant documentation. Transitioning from `requests` to `urllib` was a key workaround.  

**What I’d improve:** In the future, I would like to add visualizations or implement a stop word filter to enhance the word frequency results. I also want to explore TF-IDF and compare this article with others.  

**Biggest takeaway:** I learned how to effectively use APIs and natural language processing libraries that I hadn't utilized before. GenAI tools significantly facilitated troubleshooting and allowed me to try new things more quickly than manual searches. Moving forward, I will feel much more confident using APIs, managing packages, and structuring Python projects.