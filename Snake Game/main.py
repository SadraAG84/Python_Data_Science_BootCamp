from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(False)

x_position = [0, -20, -40]

segments = []

for snake_num in range(3):
    snake = Turtle(shape="square")
    snake.color("white")
    snake.penup()
    snake.goto(x=x_position[snake_num], y=0)
    segments.append(snake)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)


screen.exitonclick()