from turtle import Turtle, Screen
import random

screen = Screen()
Screen().setup(width=500, height=400)

race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")
print(user_bet)

colors = ["red", "orange", "purple", "green", "blue", ]
y_position = [-152, -76, 0, 76, 152]
all_turtles = []

for turtle_num in range(0, 5):
    new_tutle = Turtle(shape="turtle")
    new_tutle.color(colors[turtle_num])
    new_tutle.penup()
    new_tutle.goto(x=-230, y=y_position[turtle_num])
    all_turtles.append(new_tutle)

if user_bet:
    race_on = True
while race_on:
    for turtle in all_turtles:

        if turtle.xcor() > 230:
            race_on = False
            wining_color = turtle.pencolor()
            if user_bet == wining_color:
                print("You win the bet.")
            else:
                print(f"The {wining_color} turtle win so you lost the bet.")

        turtle_speed = random.randint(0, 10)
        turtle.forward(turtle_speed)

screen.exitonclick()
