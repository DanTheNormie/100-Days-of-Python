from turtle import Turtle, Screen

t = Turtle()
s = Screen()
s.bgcolor("black")
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']


def draw_shapes(t, count):
    sides = 3
    while count > 0:
        t.pencolor(colors[sides % 6])
        angle = 360 / sides
        for i in range(sides):
            t.fd(100)
            t.rt(angle)
        sides += 1
        count -= 1


draw_shapes(t, 10)

s.exitonclick()
