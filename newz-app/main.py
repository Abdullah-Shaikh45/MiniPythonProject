import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env if needed
load_dotenv()

query = input("What type of news are you interested in today?: ").strip()
country = input("Country code (e.g. 'us', 'in')?: ").strip().lower()
lang = input("Language code (e.g. 'en', 'hi')?: ").strip().lower()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("API Key not found. Please set it in your .env file.")
    exit()

url = f"https://gnews.io/api/v4/search?q={query}&lang={lang}&country={country}&max=10&apikey={API_KEY}"

print(f"\nFinal URL: {url}\n")
response = requests.get(url)

if response.status_code != 200:
    print("Failed to fetch news. Reason:", response.json().get("message", "Unknown error"))
    exit()

data = response.json()
articles = data.get("articles", [])

if not articles:
    print("No articles found.")
else:
    for index, article in enumerate(articles):
        print(f"{index + 1}. {article['title']}")
        print(f"   {article['url']}\n")
        print("******************************\n")
