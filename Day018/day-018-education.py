import turtle

def draw_polygon(sides, length):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.right(angle)

t = turtle.Turtle()
draw_polygon(5, 100)  # Beşgen çizer
turtle.done()