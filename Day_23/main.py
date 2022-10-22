import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()


def reset_game():
    reset_player_and_cars()

    score_board.reset_score_board()


def reset_player_and_cars():
    player.reset_player()
    car_manager.scramble_cars()


def incr_game_level():
    reset_player_and_cars()
    car_manager.incr_car_speed()
    score_board.incr_score()


screen.listen()
screen.onkeypress(player.move, "w")
screen.onkey(reset_game, "space")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars_and_recycle()

    if player.ycor() > 280:
        incr_game_level()

    for car in car_manager.list_of_cars:
        if car.distance(player) < 30:
            car_manager.stop_all_cars()
            player.stop_player()
            score_board.print_game_over()
screen.exitonclick()
