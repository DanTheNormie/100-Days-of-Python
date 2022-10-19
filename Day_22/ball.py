from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.x_speed = 10
        self.y_speed = 10
        self.ball_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto(new_x, new_y)

    def bounce_of_wall(self):
        self.y_speed *= -1

    def bounce_of_paddle(self):
        self.x_speed *= -1