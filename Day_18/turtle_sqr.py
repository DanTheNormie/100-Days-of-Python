import turtle
from turtle import *

setup(500, 500)
Screen()
turtle = turtle.Turtle()
turtle.speed(0)
showturtle()

def draw_dashed_line(t,length):
     distance_travelled = 0
     while distance_travelled < length:
         t.down()
         t.forward(5)
         t.up()
         t.forward(5)

def finish():
    done()

def up():
    turtle.setheading(90)
    draw_dashed_line(turtle,100)


def down():
    turtle.setheading(270)
    draw_dashed_line(turtle,100)


def left():
    turtle.setheading(180)
    draw_dashed_line(turtle,100)


def right():
    turtle.setheading(0)
    draw_dashed_line(turtle,100)


listen()
onkey(up, 'Up')
onkey(down, 'Down')
onkey(left, 'Left')
onkey(right, 'Right')

mainloop()
# for i in range(4):
#     timmy.fd(100)
#     timmy.rt(90)






