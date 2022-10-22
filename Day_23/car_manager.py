import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.list_of_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.create_random_cars()

    def create_random_cars(self):
        for i in range(15):
            car_color = COLORS[i % 6]
            car_x = random.randint(-280, 280)
            car_y = random.randint(-250, 250)
            new_car = Turtle(shape="square")
            new_car.shapesize(1, 2)
            new_car.pu()
            new_car.speed("fastest")
            new_car.goto(car_x, car_y)
            new_car.color(car_color)
            new_car.setheading(180)
            self.list_of_cars.append(new_car)

    def move_cars_and_recycle(self):
        for car in self.list_of_cars:
            car.forward(self.car_speed)
            if car.xcor() < -310:
                car.hideturtle()
                car.goto(320, random.randint(-250, 250))
                car.showturtle()

    def stop_all_cars(self):
        self.car_speed = 0

    def scramble_cars(self):
        for car in self.list_of_cars:
            car.hideturtle()
            car.goto(random.randint(-280, 280), random.randint(-250, 250))
            car.showturtle()
        self.car_speed = STARTING_MOVE_DISTANCE

    def incr_car_speed(self):
        self.car_speed += MOVE_INCREMENT