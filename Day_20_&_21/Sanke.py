from turtle import Turtle, Screen
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Sanke:

    def __init__(self, scrn, food, scoreboard):

        self.snake_body = []
        self.turn_point_counter_list = [0]
        self.food = food
        self.scoreboard = scoreboard
        self.speed = 2
        self.turn_counter = 0
        self.turn_points = []
        self.game_on = True
        self.scrn = scrn
        self.create_snake()
        self.head = self.snake_body[0]
        self.create_screen()

    def create_snake(self):
        head = Turtle("circle")
        head.speed("fastest")
        head.pu()
        head.shapesize(0.9)
        head.color("green")
        self.snake_body = [head]
        self.incr_snake_length(12, True)

    def create_screen(self):
        self.scrn.tracer(0)

    def close(self):
        self.scrn.bye()

    def incr_snake_length(self, num, is_first_time=False):
        if is_first_time:
            offset = 15
        else:
            offset = 0
        for i in range(num):
            self.turn_point_counter_list.append(0)
            turt = Turtle(shape="square", visible=False)
            turt.speed("fastest")
            turt.pu()
            turt.color("green")
            last_t_position = self.snake_body[len(self.snake_body) - 1].pos()
            turt.goto(last_t_position[0] - offset, last_t_position[1])
            turt.showturtle()
            self.snake_body.append(turt)

    def detect_collision_with_food(self):
        if self.head.distance(self.food) < 15:
            self.update_scoreboard()
            self.food.goto_random_pos()
            self.incr_snake_length(1)

    def detect_collision_with_wall(self):
        if abs(self.head.xcor()) > (self.scrn.window_width() / 2) - 15 or \
                abs(self.head.ycor()) > (self.scrn.window_height() / 2) - 15:
            self.scoreboard.game_over()
            self.game_on = False

    def detect_collision_with_self(self):
        for i in self.snake_body[1:]:
            if self.head.distance(i) < 10:
                self.scoreboard.game_over()
                self.game_on = False

    def start_listening_to_keystrokes(self):
        self.scrn.listen()
        self.scrn.onkey(self.move_up, "w")
        self.scrn.onkey(self.move_left, "a")
        self.scrn.onkey(self.move_down, "s")
        self.scrn.onkey(self.move_right, "d")
        self.scrn.onkey(self.close, "space")
        self.scrn.exitonclick()

    def move_up(self):
        if not self.head.heading() == DOWN:
            self.move("up")

    def move_down(self):
        if not self.head.heading() == UP:
            self.move("down")

    def move_left(self):
        if not self.head.heading() == RIGHT:
            self.move("left")

    def move_right(self):
        if not self.head.heading() == LEFT:
            self.move("right")

    def move(self, heading):
        _heading = 0
        if heading == "left":
            _heading = 180
        elif heading == "up":
            _heading = 90
        elif heading == "down":
            _heading = 270

        head_pos = self.head.pos()

        self.turn_points.append((head_pos, _heading))
        self.head.setheading(_heading)
        while self.game_on:
            self.move_1()
            self.detect_collision_with_food()
            self.detect_collision_with_wall()
            self.detect_collision_with_self()

    def move_1(self):
        self.scrn.update()
        time.sleep(0.16)
        prev_pos = self.head.pos()
        prev_pos_2 = (0, 0)
        self.head.fd(15)
        for i in range(1, len(self.snake_body)):
            prev_pos_2 = self.snake_body[i].pos()
            self.snake_body[i].goto(prev_pos)
            prev_pos = prev_pos_2

    def update_scoreboard(self):
        self.scoreboard.score += 1
        self.scoreboard.write_score()
