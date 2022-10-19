from Sanke import Sanke
from turtle import Screen
from food import Food
from scoreboard import ScoreBoard

scrn = Screen()
food = Food()
score_board = ScoreBoard(scrn)
snake = Sanke(scrn, food, score_board)

snake.start_listening_to_keystrokes()
