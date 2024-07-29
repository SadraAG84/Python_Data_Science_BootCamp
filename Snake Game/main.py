from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

x_position = [0, -20, -40]

for snake_num in range(3):
    snake = Turtle(shape="square")
    snake.color("white")
    snake.goto(x=x_position[snake_num], y=0 )














screen.exitonclick()