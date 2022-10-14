from turtle import Turtle, Screen

tim = Turtle()
scrn = Screen()
is_pen_up = False


def move_fwd():
    tim.forward(5)


def move_bck():
    tim.forward(5)


def turn_right():
    tim.right(5)


def turn_left():
    tim.left(5)


def toggle_pen():
    if tim.pen().get('pendown'):
        tim.pu()
    else:
        tim.pd()

def clr_scr():
    tim.pu()
    tim.clear()
    tim.home()
    tim.pd()




scrn.listen()

scrn.onkeypress(move_fwd, "w")
scrn.onkeypress(move_bck, "s")
scrn.onkeypress(turn_right, "d")
scrn.onkeypress(turn_left, "a")
scrn.onkey(toggle_pen, "space")
scrn.onkey(clr_scr,"c")

scrn.exitonclick()
