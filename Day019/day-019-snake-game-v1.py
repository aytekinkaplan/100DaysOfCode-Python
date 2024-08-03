import turtle
import random
import time

# Screen setup
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Advanced Snake Game")
screen.bgcolor("black")
screen.tracer(0)

# Load background image
try:
    screen.bgpic("forest_background.gif")  # Make sure to have this image in your working directory
except turtle.TurtleGraphicsError:
    print("Background image not found. Make sure 'forest_background.gif' is in the working directory.")

# Draw border
border = turtle.Turtle()
border.color("white")
border.penup()
border.goto(-300, 300)
border.pendown()
border.pensize(3)
for _ in range(4):
    border.forward(600)
    border.right(90)
border.hideturtle()

# Snake head
head = turtle.Turtle()
head.shape("triangle")
head.color("lime green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake body
segments = []

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Scoreboard
score = 0
high_score = 0
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

# Game over text
game_over_text = turtle.Turtle()
game_over_text.color("red")
game_over_text.penup()
game_over_text.hideturtle()
game_over_text.goto(0, 0)

# Snake movements
def go_up():
    if head.direction != "down":
        head.direction = "up"
        head.setheading(90)

def go_down():
    if head.direction != "up":
        head.direction = "down"
        head.setheading(270)

def go_left():
    if head.direction != "right":
        head.direction = "left"
        head.setheading(180)

def go_right():
    if head.direction != "left":
        head.direction = "right"
        head.setheading(0)

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Key bindings
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# Main game loop
while True:
    screen.update()

    # Check collision with walls
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        game_over_text.write("GAME OVER", align="center", font=("Courier", 36, "bold"))
        time.sleep(1)
        game_over_text.clear()
        head.goto(0, 0)
        head.direction = "stop"
        head.setheading(0)
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        score_display.clear()
        score_display.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Check collision with food
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("dark green")
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        if score > high_score:
            high_score = score
        score_display.clear()
        score_display.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Move the snake body
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check collision with body
    for segment in segments:
        if segment.distance(head) < 20:
            game_over_text.write("GAME OVER", align="center", font=("Courier", 36, "bold"))
            time.sleep(1)
            game_over_text.clear()
            head.goto(0, 0)
            head.direction = "stop"
            head.setheading(0)
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            score_display.clear()
            score_display.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    time.sleep(0.1)

screen.mainloop()
