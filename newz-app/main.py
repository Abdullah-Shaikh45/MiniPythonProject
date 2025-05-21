import requests
import os
from dotenv import load_dotenv

load_dotenv()
query = input("What type of newz are you interested in today?\n").strip()

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-04-18&sortBy=publishedAt&apiKey={os.getenv("API_KEY")}"

print(url)
r = requests.get(url)

data = r.json()
articles = data['articles']

for index, article in enumerate(articles):
  print(index + 1, article['title'], article['url'])
  print("\n******************************\n")
