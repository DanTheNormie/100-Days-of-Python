from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

scrn = Screen()
scrn.setup(600, 800)
scrn.bgcolor("black")
turtle_list = []


def create_turtles(num):
    for i in range(num):
        t = Turtle("turtle")
        t.color(colors[i % 6])

        turtle_list.append(t)
    return turtle_list


def set_to_starting_pos():
    width = scrn.window_width()
    height = scrn.window_height()
    # offset = (scrn.window_height() * 0.1)  # 10% of screen_height
    #
    # starting_y = int((height / 2) - offset)
    # height_after_offset = starting_y * 2
    # space = (height_after_offset) / len(turtle_list)
    # starting_y -= space / 2
    # y_coord = starting_y * -1

    no_of_turtles = len(turtle_list)
    pad_percent = 0.1
    x = height * (0.5 - pad_percent)
    space_between = (2 * x) / no_of_turtles
    y_coord = (x * (no_of_turtles - 1) / no_of_turtles) * -1

    x_coord = (int(width / 2) * -1) + 15

    for t in turtle_list:
        curr_turtle_color = t.color()[1]
        if curr_turtle_color == "blue":
            t.goto(0, y_coord)
        else:
            t.goto(x_coord, y_coord)
        y_coord += space_between


def start_race(u_bet):

    while True:
        for t in turtle_list:
            t.fd(random.randint(0, 10))
            position = t.pos()[0]
            if position >= (scrn.window_width() / 2):

                curr_turtle_color = t.color()[1]
                if u_bet == curr_turtle_color:
                    print("You win.")
                else:
                    print(f"You lose\n You bet on {u_bet}\n Winner is {curr_turtle_color}")
                return


create_turtles(5)

set_to_starting_pos()

user_bet = scrn.textinput(title="Make your bet !!!",
                          prompt="Which turtle do you think will win the race? Enter a color : ").lower()

if user_bet:
    start_race(user_bet)


scrn.exitonclick()
