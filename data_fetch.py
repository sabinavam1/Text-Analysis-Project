# data_fetch.py
import urllib.request
import json

def fetch_wikipedia_text(title):
    api_url = f"https://en.wikipedia.org/w/api.php?action=query&titles={title}&prop=extracts&explaintext&format=json"
    with urllib.request.urlopen(api_url) as response:
        data = json.loads(response.read())
        page = next(iter(data["query"]["pages"].values()))
        return page["extract"]
