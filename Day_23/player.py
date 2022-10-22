from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.speed("fastest")
        self.player_speed = MOVE_DISTANCE
        self.pu()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.fd(self.player_speed)

    def reset_player(self):
        self.goto(STARTING_POSITION)
        self.player_speed = MOVE_DISTANCE

    def stop_player(self):
        self.player_speed = 0
