import requests
from bs4 import BeautifulSoup

url = "https://www.empireonline.com/movies/features/best-movies-2/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")

def clean_title(title):
    # Başındaki sayıları ve noktalamayı kaldır
    parts = title.split(') ', 1)
    if len(parts) > 1:
        return parts[1].strip()
    return title.strip()

movie_titles = [clean_title(movie.getText()) for movie in all_movies]

# Listeyi ters çevir (100'den 1'e)
movie_titles.reverse()

print("Empire'ın Tüm Zamanların En İyi 100 Filmi Listesi")
print("=" * 50)
for i, title in enumerate(movie_titles, 1):
    print(f"{i:3}. {title}")

# Sonuçları bir dosyaya kaydet
with open("en_iyi_100_film.txt", "w", encoding="utf-8") as file:
    file.write("Empire'ın Tüm Zamanların En İyi 100 Filmi Listesi\n")
    file.write("=" * 50 + "\n")
    for i, title in enumerate(movie_titles, 1):
        file.write(f"{i:3}. {title}\n")

print("\nSonuçlar 'en_iyi_100_film.txt' dosyasına kaydedildi.")