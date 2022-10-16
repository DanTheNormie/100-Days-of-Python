from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class ScoreBoard(Turtle):

    def __init__(self, scrn):
        super().__init__()
        self.score = 17
        self.scrn = scrn
        self.pu()
        self.hideturtle()
        self.goto(0, (scrn.window_height() / 2) - 30)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f"Your score is {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write(arg=f"Game Over :(", align=ALIGNMENT, font=FONT)