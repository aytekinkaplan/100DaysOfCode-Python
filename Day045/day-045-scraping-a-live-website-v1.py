from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all("span", class_="titleline")

article_texts = []
article_links = []
article_upvotes = []

for article in articles:
    # Başlık ve link
    a_tag = article.find("a")
    if a_tag:
        text = a_tag.getText()
        article_texts.append(text)
        link = a_tag.get("href")
        article_links.append(link)

    # Upvotes
    score_span = article.find_next("span", class_="score")
    if score_span:
        upvotes = int(score_span.getText().split()[0])
        article_upvotes.append(upvotes)
    else:
        article_upvotes.append("0")

print(article_texts)
print(article_links)
print(article_upvotes)

# Finding the largest upvote
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])
