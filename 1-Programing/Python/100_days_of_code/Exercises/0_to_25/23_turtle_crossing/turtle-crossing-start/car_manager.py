from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.all_cars =  []
        self.car_speed = STARTING_MOVE_DISTANCE  # We want to increase the speed each time the turtle crosses the line, this will help to do it.

    def create_car(self):
        random_chance = random.randint(1, 6) # Without this, too many cars are created. This reduces the creation to a tolerable amount
        if random_chance == 1: # giving the turtle the option to have space to walk through the cars.
            new_car = Turtle("square")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)  # Choses between -250 and 250 a nunber that will be use below.
            new_car.goto(300, random_y)  # This will generate the car in the indicated cordinates.
            self.all_cars.append(new_car) 

    def move_cars(self): # Function to make the cars to move.
        for car in self.all_cars: # Iterates in the car list 
            car.backward(self.car_speed) # and makes the car to move to the left. The speed is provided 

    # Each time the turtle croses the line will increase the speed of the cars by +10 pixels
    def level_up(self):
        self.car_speed += MOVE_INCREMENT