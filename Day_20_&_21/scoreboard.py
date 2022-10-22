from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class ScoreBoard(Turtle):

    def __init__(self, scrn):
        super().__init__()
        self.score = 0
        self.highscore = self.get_highscore()
        self.scrn = scrn
        self.pu()
        self.hideturtle()
        self.write_score()
        self.write_highscore()

    def write_score(self):
        self.clear()
        self.goto(-100, (self.scrn.window_height() / 2) - 30)
        self.write(arg=f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def write_highscore(self):
        self.goto(100, (self.scrn.window_height() / 2) - 30)
        self.write(arg=f"Highscore : {self.highscore}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write(arg=f"Game Over :(", align=ALIGNMENT, font=FONT)

    def get_highscore(self):
        file = open("data.txt", mode="r")
        highscore = int(file.read())
        file.close()
        return highscore

    def set_highscore(self):
        file = open("data.txt",mode="w")
        file.write(f"{self.highscore}")
        file.close()