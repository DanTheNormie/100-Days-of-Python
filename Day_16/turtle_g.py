import turtle

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
def loopSqr(turle, times):

    x = 1
    y = 2
    turle.pensize(2)

    for i in range(times):
        turle.pencolor(colors[i%4])
        for j in range(2):
            turle.forward(x * i)
            turle.left(90)
        for k in range(2):
            turle.forward(y * i)
            turle.left(90)
        x = y
        y += 1


akarsh = turtle.Turtle("classic")
scrn = turtle.Screen()
akarsh.color("LightSkyBlue")
scrn.bgcolor("black")
akarsh.speed(500)
loopSqr(akarsh, 500)

scrn.exitonclick()
