from bs4 import BeautifulSoup
import requests
from datetime import datetime


while True:
    date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    try:
        datetime.strptime(date, '%Y-%m-%d')
        break
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")


titles = soup.select("li ul li h3.c-title")

if not titles:
    print("No songs found. The website structure might have changed.")
else:
    filename = f"100-billboard-top-100-songs-{date}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        for i, title in enumerate(titles, 1):
            song_title = title.get_text(strip=True)
            file.write(f"{i}. {song_title}\n")

    print(f"Successfully saved {len(titles)} songs to {filename}")