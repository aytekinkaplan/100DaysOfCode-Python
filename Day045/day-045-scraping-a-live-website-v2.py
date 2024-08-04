from bs4 import BeautifulSoup
import requests
from functools import reduce

response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")

# Makaleleri bulma
articles = soup.find_all("span", class_="titleline")

# Başlık ve linkleri alma
get_text_and_link = lambda a: (a.getText(), a.get("href"))
article_data = list(map(lambda article: get_text_and_link(article.find("a")), articles))

# Upvote'ları alma
get_upvotes = lambda article: int(article.find_next("span", class_="score").getText().split()[0]) if article.find_next("span", class_="score") else 0
upvotes = list(map(get_upvotes, articles))

# Verileri birleştirme
combined_data = list(zip(article_data, upvotes))

# En çok oy alan makaleyi bulma
max_upvote_article = reduce(lambda x, y: x if x[1] > y[1] else y, combined_data)

# Sonuçları yazdırma
print("Tüm başlıklar:", list(map(lambda x: x[0][0], combined_data)))
print("Tüm linkler:", list(map(lambda x: x[0][1], combined_data)))
print("Tüm upvote'lar:", upvotes)

print("\nEn çok oy alan makale:")
print("Başlık:", max_upvote_article[0][0])
print("Link:", max_upvote_article[0][1])
print("Upvote sayısı:", max_upvote_article[1])