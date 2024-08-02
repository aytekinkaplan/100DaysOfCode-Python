import turtle as t
from turtle import Screen
import random

# Ekranı ayarla
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Rastgele Yürüyüş")
screen.colormode(255)  # RGB renk modunu etkinleştir

# Kaplumbağayı ayarla
tim = t.Turtle()
tim.speed(0)  # En hızlı çizim hızı
tim.pensize(4)  # Çizgi kalınlığını artır


# Rastgele renk fonksiyonu
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def random_walk():
    going_forward_length = random.randint(10, 50)  # Adım uzunluğunu sınırla
    tim.color(random_color())  # Her adımda rastgele renk
    tim.forward(going_forward_length)
    tim.setheading(random.choice([0, 90, 180, 270]))


# Ana döngü
n_steps = 500  # Toplam adım sayısı
for _ in range(n_steps):
    random_walk()

    # Ekran sınırlarını kontrol et
    if abs(tim.xcor()) > 380 or abs(tim.ycor()) > 280:
        tim.penup()
        tim.goto(0, 0)  # Merkeze dön
        tim.pendown()

# Ekranı açık tut
screen.exitonclick()
