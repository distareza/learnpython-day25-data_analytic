"""
    Learn how to use Turtle Image and Pandas Module

    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.isin.html
"""
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image_bg = "blank_states_img.gif"
screen.addshape(image_bg)
turtle.shape(image_bg)


def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

import pandas

states_data = pandas.read_csv("50_states.csv")
print(states_data)

guess_states = []
while True and len(guess_states) < 50:
    try:
        answer = screen.textinput(title="Guess the states", prompt="What's another states's name ?")
        if answer == "" or answer == "exit":
            break

        if answer.title() not in states_data.state.to_list():
            print(f"{answer} not in the list")
            continue

        select_states = states_data[states_data.state == answer.title()]
        state_name = select_states.state.values[0]
        state_pos_x = int(select_states.x.values[0])
        state_pos_y = int(select_states.y.values[0])

        guess_states.append(state_name)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x=state_pos_x, y=state_pos_y)
        t.pendown()
        t.write(state_name)

    except Exception as ex:
        print(ex)
        break


print(f"Guess corrected : {guess_states}")

# Get Missing State
missing_states = states_data[~states_data.state.isin(guess_states)]
print(f"not able to guess : {missing_states.state.to_list()}")

pandas.DataFrame(missing_states.state.to_list()).to_csv("states_to_learn.csv")

