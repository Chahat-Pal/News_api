import sys
sys.stdout.reconfigure(encoding='utf-8')
import requests

#
my_api_key="YOUR_API_KEY"
query=input("what are you interested in today?")
url=f"https://newsapi.org/v2/everything?q={query}&from=2026-03-18&sortBy=publishedAt&apiKey={my_api_key}"
print(url)
r=requests.get(url)
data=r.json()
articles=data["articles"]
for index, article in enumerate(articles):
    print(index+1, article["title"], article["url"])
    print("\n***************************************************\n")