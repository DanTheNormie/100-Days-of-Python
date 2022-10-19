from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Stencil", 24, "bold")


class GameScreen(Turtle):
    def __init__(self,screen):
        super().__init__(visible=False)
        self.screen_ref = screen

        self.player_score_keeper = Turtle(visible=False)
        self.bot_score_keeper = Turtle(visible=False)
        self.net_turtle = Turtle(visible=False)

        self.player_score = 0
        self.bot_score = 0

        self.scrn_top_y = self.screen.window_height() / 2
        self.scrn_bottom_y = self.scrn_top_y * -1
        self.scrn_right_x = self.screen.window_width() / 2
        self.scrn_left_x = self.scrn_right_x * -1

        self.init_drawers()
        self.draw_game_screen()

    def init_drawers(self):
        self.screen.bgcolor("black")
        self.net_turtle.pencolor("white")
        self.bot_score_keeper.color("white")
        self.player_score_keeper.color("white")

    def draw_game_screen(self):
        self.draw_net()
        self.draw_scores()

    def draw_scores(self):
        self.draw_player_score()
        self.draw_bot_score()

    def draw_bot_score(self):
        self.bot_score_keeper.clear()
        self.bot_score_keeper.pu()
        self.bot_score_keeper.goto(self.scrn_right_x * 0.2, self.scrn_top_y - (self.scrn_top_y * 0.15))
        self.bot_score_keeper.write(arg=f"{self.bot_score}", align=ALIGNMENT, font=FONT)

    def draw_player_score(self):
        self.player_score_keeper.clear()
        self.player_score_keeper.pu()
        self.player_score_keeper.goto(self.scrn_left_x * 0.2, self.scrn_top_y - (self.scrn_top_y * 0.15))
        self.player_score_keeper.write(arg=f"{self.player_score}", align=ALIGNMENT, font=FONT)

    def draw_net(self):
        self.net_turtle.pu()
        self.net_turtle.goto(0, (self.screen.window_height() / 2) * -1)
        self.net_turtle.setheading(90)
        while self.net_turtle.pos()[1] < self.screen.window_height() / 2:
            self.net_turtle.fd(20)
            self.net_turtle.pd()
            self.net_turtle.fd(20)
            self.net_turtle.pu()
