from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.all_cars =  []

    def create_cars(self):
        new_car = Turtle("square")
        new_car.shapesize(1,2)
        new_car.penup()
        new_car.left(180)
        new_car.color(random.choice(COLORS))
        random_y = random.randint(-250, 250)
        new_car.left(90)
        new_car.goto(300, random_y)
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)
            