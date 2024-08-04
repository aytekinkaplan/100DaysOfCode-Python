from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
content = response.content

soup = BeautifulSoup(content, "html.parser")

article_tags = soup.find_all("span", class_="titleline")

article_texts = []
article_links = []

for tag in article_tags:
    a_tag = tag.find("a")
    if a_tag:
        article_texts.append(a_tag.text)
        article_links.append(a_tag.get("href"))

for i, (text, link) in enumerate(zip(article_texts, article_links), 1):
    print(f"{i}. {text}")
    print(f"   {link}")