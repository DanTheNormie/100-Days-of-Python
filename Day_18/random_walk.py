from turtle import Turtle, Screen
import random

t = Turtle()
s = Screen()
s.colormode(255)
s.bgcolor("black")
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t.pensize(5)

def generate_random_rgb_tuple():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)

    return (r,g,b)

def do_random_walk(t, num):
    count = 0
    while count < num:
        t.pencolor(generate_random_rgb_tuple())
        random_side = (90 * random.randint(1, 4)) % 360
        t.setheading(random_side)
        t.fd(50)
        count += 1


do_random_walk(t, 500)

s.exitonclick()
