import requests
import json
query = input("Which topic you want to see :")
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-02-01&sortBy=publishedAt&apiKey=4b820510697646b9849f05c18d24dd59"
r = requests.get(url)
# print(r.text);
news = json.loads(r.text)
for article in news["articles"]:
    print(f"Author of the article is :- {article['author']}")
    print(article['title'])
    print(article['description'])
    print("===========================================")