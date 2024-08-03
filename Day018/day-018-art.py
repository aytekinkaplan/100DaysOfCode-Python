import turtle
import random

t = turtle.Turtle()
t.speed(0)

for _ in range(200):
    r, g, b = random.random(), random.random(), random.random()
    t.pencolor(r, g, b)
    t.circle(random.randint(10, 100))
    t.penup()
    t.goto(random.randint(-300, 300), random.randint(-300, 300))
    t.pendown()

turtle.done()