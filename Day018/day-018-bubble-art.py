import turtle
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                draw_bars(arr)

def draw_bars(arr):
    screen.clear()
    for i, height in enumerate(arr):
        t.penup()
        t.goto(i*20 - 200, -200)
        t.pendown()
        t.forward(height * 2)

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

arr = [random.randint(10, 100) for _ in range(20)]
draw_bars(arr)
bubble_sort(arr)

screen.exitonclick()