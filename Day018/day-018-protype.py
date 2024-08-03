import turtle


def draw_circle(x, y, radius):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.circle(radius)


t = turtle.Turtle()
draw_circle(0, 0, 50)
draw_circle(-60, 60, 30)
draw_circle(60, 60, 30)

turtle.done()
