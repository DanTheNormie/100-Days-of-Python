import time
import turtle
from turtle import Screen
from pong_screen import GameScreen
from paddle import Paddle
from ball import Ball

screen = Screen()
gameScreen = GameScreen(screen)
game_on = True
player_1_paddle = Paddle(is_player=False)
player_2_paddle = Paddle(is_player=True)
ball = Ball()
screen.tracer(0)


def end_game():
    turtle.bye()


screen.listen()
screen.onkeypress(fun=player_1_paddle.go_up, key="Up")
screen.onkeypress(fun=player_1_paddle.go_down, key="Down")
screen.onkeypress(fun=player_2_paddle.go_up, key="w")
screen.onkeypress(fun=player_2_paddle.go_down, key="s")
screen.onkeypress(end_game, "space")

while game_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()
    if abs(ball.ycor()) > screen.window_height() / 2 - ((screen.window_height()/2) * 0.05):
        ball.bounce_of_wall()
    if abs(ball.xcor()) > screen.window_width() / 2 - ((screen.window_width()/2) * 0.13) and \
            (ball.distance(player_1_paddle) < 50 or
             ball.distance(player_2_paddle) < 50):
        ball.bounce_of_paddle()
        ball.ball_speed *= 0.9

    if ball.xcor() < (screen.window_width()/2)*-1:
        gameScreen.player_score += 1
        gameScreen.draw_player_score()
        ball.home()
        ball.ball_speed = 0.1
    if ball.xcor() > (screen.window_width()/2):
        gameScreen.bot_score += 1
        gameScreen.draw_bot_score()
        ball.home()
        ball.ball_speed = 0.1


screen.exitonclick()
