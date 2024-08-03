import turtle
import random
import time

# Ekran ayarları
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Yılan Oyunu")
screen.bgcolor("black")
screen.tracer(0)

# Yılan başı
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Yılan vücudu
segments = []

# Yem
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Skor
score = 0
high_score = 0
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Skor: {score} Yüksek Skor: {high_score}", align="center", font=("Courier", 24, "normal"))

# Yılan hareketleri
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Tuş atamaları
screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")

# Ana oyun döngüsü
while True:
    screen.update()

    # Çarpışma kontrolü - duvarlar
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        score_display.clear()
        score_display.write(f"Skor: {score} Yüksek Skor: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Yem yeme kontrolü
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        if score > high_score:
            high_score = score
        score_display.clear()
        score_display.write(f"Skor: {score} Yüksek Skor: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Yılan vücudunun hareketi
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Çarpışma kontrolü - vücut
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            score_display.clear()
            score_display.write(f"Skor: {score} Yüksek Skor: {high_score}", align="center", font=("Courier", 24, "normal"))

    time.sleep(0.1)

screen.mainloop()