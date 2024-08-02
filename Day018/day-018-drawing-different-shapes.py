import turtle as t
from turtle import Screen

tim = t.Turtle()


def draw_shape(sides, length):
    angle = 360 / sides
    for _ in range(sides):
        tim.forward(length)
        tim.right(angle)


for shape_side_n_length in [(3, 100), (4, 100), (5, 100), (6, 100), (7, 100), (8, 100)]:
    draw_shape(*shape_side_n_length)


def draw_shape_with_colors(sides, length, color):
    tim.color(color)
    angle = 360 / sides
    for _ in range(sides):
        tim.forward(length)
        tim.right(angle)


for shape_side_n_length_color in [(3, 100, "red"), (4, 100, "green"), (5, 100, "blue")]:
    draw_shape_with_colors(*shape_side_n_length_color)

screen = Screen()
screen.exitonclick()
