import requests
import json

query=input("what type of news are you interested in ?")
url=f"https://newsapi.org/v2/everything?q={query}&from=2023-04-21&sortBy=publishedAt&apiKey=4626892587c640139a2da23518cd268d"

r=requests.get(url)
news=json.loads(r.text)
#print(news,type(news))
for article in news["articles"]:
  print(article["title"])
  print(article["description"])
  print("______________________________________")


