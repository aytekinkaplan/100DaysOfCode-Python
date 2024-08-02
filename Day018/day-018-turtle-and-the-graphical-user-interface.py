from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")


def draw_shape_square():
    for _ in range(4):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(90)


draw_shape_square()
draw_shape_square()
draw_shape_square()
draw_shape_square()
draw_shape_square()

screen = Screen()
screen.exitonclick()
