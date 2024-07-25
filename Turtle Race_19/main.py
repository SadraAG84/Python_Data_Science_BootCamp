from turtle import Turtle, Screen

screen = Screen()
Screen().setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")
print(user_bet)

colors = ["red", "orange", "purple", "green", "blue", ]
y_position = [-152, -76, 0, 76, 152]

for turtle_num in range(0, 5):
    tutle = Turtle(shape="turtle")
    tutle.color(colors[turtle_num])
    tutle.penup()
    tutle.goto(x=-230, y=y_position[turtle_num])

screen.exitonclick()
