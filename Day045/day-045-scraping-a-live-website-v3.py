from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime

# Web sayfasını çekme ve parse etme
response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")

# Makaleleri bulma
articles = soup.find_all("span", class_="titleline")

# Veri toplama
data = []
for article in articles:
    a_tag = article.find("a")
    if a_tag:
        title = a_tag.getText()
        link = a_tag.get("href")
        score_span = article.find_next("span", class_="score")
        upvotes = int(score_span.getText().split()[0]) if score_span else 0
        data.append({"title": title, "link": link, "upvotes": upvotes})

# DataFrame oluşturma
df = pd.DataFrame(data)

# Basit analizler
df['word_count'] = df['title'].apply(lambda x: len(x.split()))
df['domain'] = df['link'].apply(lambda x: x.split('/')[2] if x.startswith('http') else 'N/A')

# En çok oy alan 5 makale
top_5_articles = df.nlargest(5, 'upvotes')

# Ortalama upvote ve kelime sayısı
avg_upvotes = df['upvotes'].mean()
avg_word_count = df['word_count'].mean()

# En sık görülen domainler
top_domains = df['domain'].value_counts().head()

# Analiz sonuçlarını DataFrame'e ekleme
analysis_df = pd.DataFrame({
    'Metric': ['Average Upvotes', 'Average Word Count'],
    'Value': [avg_upvotes, avg_word_count]
})

# Excel dosyasına kaydetme
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
excel_filename = f"hacker_news_analysis_{timestamp}.xlsx"

with pd.ExcelWriter(excel_filename) as writer:
    df.to_excel(writer, sheet_name='Raw Data', index=False)
    top_5_articles.to_excel(writer, sheet_name='Top 5 Articles', index=False)
    analysis_df.to_excel(writer, sheet_name='Analysis', index=False)
    top_domains.to_excel(writer, sheet_name='Top Domains')

print(f"Analysis saved to {excel_filename}")

# Bazı sonuçları konsola yazdırma
print("\nTop 5 Articles:")
print(top_5_articles[['title', 'upvotes']])
print(f"\nAverage Upvotes: {avg_upvotes:.2f}")
print(f"Average Word Count: {avg_word_count:.2f}")
print("\nTop Domains:")
print(top_domains)