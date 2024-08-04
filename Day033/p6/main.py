import requests
from datetime import datetime
from tkinter import Tk, Label, LEFT

# Koordinatlar
MY_LAT = 38.503490
MY_LNG = 43.396450

# API parametreleri
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

# API isteği
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

# Zamanları parse et
sunrise = datetime.fromisoformat(data["results"]["sunrise"]).time()
sunset = datetime.fromisoformat(data["results"]["sunset"]).time()
day_length = data["results"]["day_length"]
civil_twilight_begin = datetime.fromisoformat(data["results"]["civil_twilight_begin"]).time()
civil_twilight_end = datetime.fromisoformat(data["results"]["civil_twilight_end"]).time()
nautical_twilight_begin = datetime.fromisoformat(data["results"]["nautical_twilight_begin"]).time()
nautical_twilight_end = datetime.fromisoformat(data["results"]["nautical_twilight_end"]).time()
astronomical_twilight_begin = datetime.fromisoformat(data["results"]["astronomical_twilight_begin"]).time()
astronomical_twilight_end = datetime.fromisoformat(data["results"]["astronomical_twilight_end"]).time()
status = data["status"]

# Açıklamalar
explanation = (
    f"Gün Doğumu: {sunrise} - Güneşin doğduğu zaman.\n"
    f"Gün Batımı: {sunset} - Güneşin battığı zaman.\n"
    f"Gün Uzunluğu: {day_length} - Günün toplam uzunluğu (saat:dakika:saniye).\n"
    f"Sivil Alacakaranlık Başlangıcı: {civil_twilight_begin} - Sivil alacakaranlığın başladığı zaman.\n"
    f"Sivil Alacakaranlık Sonu: {civil_twilight_end} - Sivil alacakaranlığın bittiği zaman.\n"
    f"Deniz Alacakaranlığı Başlangıcı: {nautical_twilight_begin} - Deniz alacakaranlığının başladığı zaman.\n"
    f"Deniz Alacakaranlığı Sonu: {nautical_twilight_end} - Deniz alacakaranlığının bittiği zaman.\n"
    f"Astronomik Alacakaranlık Başlangıcı: {astronomical_twilight_begin} - Astronomik alacakaranlığın başladığı zaman.\n"
    f"Astronomik Alacakaranlık Sonu: {astronomical_twilight_end} - Astronomik alacakaranlığın bittiği zaman.\n"
    f"Durum: {status} - API isteğinin durumu (OK veya hata durumu)."
)

# GUI ayarları
root = Tk()
root.title("Gün Doğumu ve Batımı Bilgileri")

# GUI açıklamaları
Label(root, text="Gün Doğumu ve Batımı Bilgileri", font=("Helvetica", 16, "bold")).pack(pady=10)
Label(root, text=explanation, justify=LEFT, font=("Helvetica", 12)).pack(padx=10, pady=10)

root.mainloop()
