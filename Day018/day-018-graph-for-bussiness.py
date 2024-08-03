import turtle

def draw_bar(height, x_pos, color):
    t.penup()
    t.goto(x_pos, 0)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(40)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

data = [("A", 100, "red"), ("B", 150, "blue"), ("C", 80, "green"), ("D", 200, "yellow")]

for i, (label, value, color) in enumerate(data):
    draw_bar(value, i * 60 - 100, color)
    t.penup()
    t.goto(i * 60 - 80, -20)
    t.write(label, align="center")

screen.exitonclick()