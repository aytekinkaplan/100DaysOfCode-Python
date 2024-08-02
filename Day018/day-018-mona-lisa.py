import turtle as t
from turtle import Screen

# Ekranı ayarla
screen = Screen()
screen.setup(width=400, height=400)

# Kaplumbağayı oluştur
tim = t.Turtle()
tim.speed(2)  # Çizim hızını ayarla

# Yüz çerçevesi
tim.penup()
tim.goto(-100, 100)
tim.pendown()
tim.circle(100)

# Gözler
tim.penup()
tim.goto(-40, 120)
tim.pendown()
tim.circle(15)
tim.penup()
tim.goto(40, 120)
tim.pendown()
tim.circle(15)

# Burun
tim.penup()
tim.goto(0, 80)
tim.pendown()
tim.right(90)
tim.forward(20)

# Ağız
tim.penup()
tim.goto(-40, 40)
tim.pendown()
tim.setheading(-60)
tim.circle(50, 120)

# Saç
tim.penup()
tim.goto(-100, 100)
tim.pendown()
tim.setheading(45)
for _ in range(10):
    tim.forward(20)
    tim.penup()
    tim.forward(5)
    tim.pendown()

# Ekranı aç tut
screen.exitonclick()