from turtle import Turtle, Screen
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Sanke:

    def __init__(self):

        self.snake_body = []
        self.turn_point_counter_list = [0]

        self.speed = 2
        self.turn_counter = 0
        self.turn_points = []
        self.scrn = Screen()
        self.create_snake()
        self.head = self.snake_body[0]
        self.create_screen()

    def create_snake(self):
        head = Turtle("circle")
        head.speed("fastest")
        head.shapesize(0.9)
        head.color("green")
        self.snake_body = [head]
        self.incr_snake_length(12)

    def create_screen(self):
        self.scrn.tracer(0)

    def close(self):
        self.scrn.bye()

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
            while True:
                self.move("up")

    def move_down(self):
        if not self.head.heading() == UP:
            while True:
                self.move("down")

    def move_left(self):
        if not self.head.heading() == RIGHT:
            while True:
                self.move("left")

    def move_right(self):
        if not self.head.heading() == LEFT:
            while True:
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


        self.move_2()


    def move_2(self):
        self.scrn.update()
        self.head.fd(self.speed)
        for i in range(1, len(self.snake_body)):
            turn_point_list_index = self.turn_point_counter_list[i]
            if turn_point_list_index < len(self.turn_points):
                turn_point = self.turn_points[turn_point_list_index][0]
                turn_heading = self.turn_points[turn_point_list_index][1]
                if self.snake_body[i].pos() == turn_point:
                    self.snake_body[i].setheading(turn_heading)
                    self.turn_point_counter_list[i] += 1

                elif turn_heading == UP or turn_heading == DOWN:
                    if self.snake_body[i].heading() == LEFT:
                        if (self.snake_body[i].xcor() - self.speed) < turn_point[0]:
                            self.snake_body[i].goto(turn_point)
                            self.snake_body[i].setheading(turn_heading)
                            self.turn_point_counter_list[i] += 1
                            continue

                    elif self.snake_body[i].heading() == RIGHT:
                        if (self.snake_body[i].xcor() + self.speed) > turn_point[0]:
                            self.snake_body[i].goto(turn_point)
                            self.snake_body[i].setheading(turn_heading)
                            self.turn_point_counter_list[i] += 1
                            continue

                elif turn_heading == LEFT or turn_heading == RIGHT:
                    if self.snake_body[i].heading() == DOWN:
                        if (self.snake_body[i].ycor() - self.speed) < turn_point[1]:
                            self.snake_body[i].goto(turn_point)
                            self.snake_body[i].setheading(turn_heading)
                            self.turn_point_counter_list[i] += 1
                            continue

                    elif self.snake_body[i].heading() == UP:
                        if (self.snake_body[i].ycor() + self.speed) > turn_point[1]:
                            self.snake_body[i].goto(turn_point)
                            self.snake_body[i].setheading(turn_heading)
                            self.turn_point_counter_list[i] += 1
                            continue

            self.snake_body[i].fd(self.speed)
        # while True:
        #     self.scrn.update()
        #     time.sleep(0.06)
        #     prev_pos = self.head.pos()
        #     prev_pos_2 = (0, 0)
        #     self.head.setheading(_heading)
        #     self.head.fd(15)
        #     for i in range(1, len(self.snake_body)):
        #         prev_pos_2 = self.snake_body[i].pos()
        #         self.snake_body[i].goto(prev_pos)
        #         prev_pos = prev_pos_2

    def incr_snake_length(self, num):
        for i in range(num):
            self.turn_point_counter_list.append(0)
            turt = Turtle("square")
            turt.speed("fastest")
            turt.color("green")
            last_t_position = self.snake_body[len(self.snake_body) - 1].pos()
            turt.goto(last_t_position[0] - 15, last_t_position[1])
            self.snake_body.append(turt)
