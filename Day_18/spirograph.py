from turtle import Turtle, Screen
import random

t = Turtle()
s = Screen()
s.colormode(255)
s.bgcolor("black")


def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)

    return r, g, b


i = 1
while i <= 360:
    t.pencolor(random_color())
    t.circle(50)
    t.seth(i)
    i += 5
