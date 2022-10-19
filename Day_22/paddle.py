from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, is_player=False):
        super().__init__(visible=False)
        self.speed = 20
        self.shape("square")
        self.shapesize(1, 5)
        self.seth(90)
        self.color("white")
        self.pu()

        if is_player:
            self.goto(((self.screen.window_width() / 2) * -1) + ((self.screen.window_width()/2) * 0.1), 0)
        else:
            self.goto((self.screen.window_width() / 2) - ((self.screen.window_width()/2) * 0.1), 0)

        self.showturtle()

    def go_up(self):
        self.fd(self.speed)

    def go_down(self):
        self.bk(self.speed)
