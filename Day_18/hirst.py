from turtle import Turtle, Screen
from random import choice
import colorgram

colors_list = [(104, 91, 229), (252, 141, 56), (200, 72, 176), (92, 150, 220), (231, 99, 195), (254, 211, 61),
               (172, 38, 156), (141, 16, 158), (42, 25, 148), (88, 233, 194)]

t = Turtle()
s = Screen()
s.colormode(255)
s.bgcolor("black")
t.penup()
t.speed("fastest")
t.setposition(-500, -500)

for i in range(11):
    t.setheading(0)
    for _ in range(10):
        t.dot(20, choice(colors_list))
        t.fd(50)
    t.home()
    t.setheading(90)
    t.forward(50 * i)
s.exitonclick()
