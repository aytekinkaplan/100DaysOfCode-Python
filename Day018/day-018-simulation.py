import turtle
import random

def move_particle():
    angle = random.randint(0, 360)
    distance = random.randint(1, 10)
    t.right(angle)
    t.forward(distance)
    screen.ontimer(move_particle, 100)

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

move_particle()

screen.mainloop()