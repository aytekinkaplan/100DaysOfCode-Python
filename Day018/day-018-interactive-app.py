import turtle

def move_forward():
    t.forward(10)

def turn_left():
    t.left(90)

t = turtle.Turtle()
screen = turtle.Screen()

screen.onkey(move_forward, "Up")
screen.onkey(turn_left, "Left")
screen.listen()

turtle.done()