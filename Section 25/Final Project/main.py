import turtle as td
import pandas as pd

screen = td.Screen()
screen.title("U.S. States Game")
image = "Final Project/Recourses/blank_states_img.gif"
data = pd.read_csv("Final Project/Recourses/50_states.csv")

screen.addshape(image)
td.shape(image)

# {{
## With this function we can get the coordinate of any dot of image


# def get_mouse_click_coor(x, y):
#     print(x, y)

# td.onscreenclick(get_mouse_click_coor)
# screen.mainloop()

## We don't use this function here because we had listed the coordinate before on csv file

# screen.exitonclick()
## We use screen.mainloop() to keep screen open after we click
# }}


def get_input():
    global user_answer 
    user_answer = screen.textinput(title= f"{len(guessed_list)}/50 is correct", prompt= "What's another state's name? ")
    user_answer = user_answer.title()

data_list = data.state.to_list()
print(data_list)

guessed_list = []
def check_answer():

    if user_answer in data_list:
        t = td.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_answer]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(user_answer)
        guessed_list.append(user_answer)
        

while len(guessed_list) <= 50:
    get_input()
    check_answer()
    if user_answer == "Exit":
        missed_states = []
        for miss_states in data_list:
            if miss_states not in guessed_list:
                missed_states.append(miss_states)
        new_data = pd.DataFrame(missed_states)
        new_data.to_csv("missed_states.csv")
        break

screen.exitonclick()