import turtle
import math

# Sine wave
t = turtle.Turtle()
for angle in range(360):
    y = math.sin(math.radians(angle))
    t.goto(angle, y * 100)
turtle.done()
print("\n")

# Cosine wave
t = turtle.Turtle()
for angle in range(360):
    y = math.cos(math.radians(angle))
    t.goto(angle, y * 100)
turtle.done()
print("\n")
