from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.score = 1
        self.pu()
        self.goto(-280, 250)
        self.write(arg=f"Level {self.score}", font=FONT)

    def incr_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Level {self.score}", font=FONT)

    def print_game_over(self):
        self.home()
        self.write(arg=f"Game Over :(", font=FONT, align="center")

    def reset_score_board(self):
        self.clear()
        self.score = 1
        self.goto(-280, 250)
        self.write(arg=f"Level {self.score}", font=FONT)