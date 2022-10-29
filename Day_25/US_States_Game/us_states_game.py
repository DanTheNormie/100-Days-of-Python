import turtle
import pandas

screen = turtle.Screen()
screen.screensize(720, 490)
screen.title("U.S. States Game")
image_path = "blank_states_img.gif"
screen.addshape(image_path)

writer = turtle.Turtle(visible=False)
writer.pu()

writer2 = turtle.Turtle(visible=False)
writer2.pu()

guessed_states_list = []

turtle.shape(image_path)

states_csv = pandas.read_csv("50_states.csv")

all_states_list = states_csv.state.tolist()

answer = ""


def guess_answer(answer):
    state_info = states_csv[states_csv["state"] == answer]
    if len(state_info) == 1:
        writer2.clear()
        x = int(state_info.x)
        y = int(state_info.y)
        writer.goto(x, y)
        writer.write(f"{answer}")
        guessed_states_list.append(answer)
    else:
        writer2.home()
        writer2.write(f"You guessed wrong. !!!")


for i in range(0, 50):
    if i == 0:
        title = "Guess the State"
    else:
        title = f" {len(guessed_states_list)}/50 States Correct"

    answer = screen.textinput(title=f"{title}", prompt="What's another state's name ?").title()
    if answer.lower() == "exit":
        missed_state = []
        for state in all_states_list:
            if state not in guessed_states_list:
                missed_state.append(state)

        missed_states_data_frame = pandas.DataFrame(missed_state)
        missed_states_data_frame.to_csv("missed_states.csv")
        break
    guess_answer(answer)


def get_x_y(x, y):
    print(x, y)


turtle.onscreenclick(get_x_y)

screen.mainloop()
