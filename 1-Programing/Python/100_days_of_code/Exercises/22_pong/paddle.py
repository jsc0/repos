from turtle import Turtle

STARTING_POSITION = [(360,-20), (360,0), (360,20)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle:

    def __init__(self):
        self.segments = []
        self.create_paddle()
        self.head = self.segments[0]

# Fuction to create the paddle.We iterate the STARTING_POSITION constant 
    def create_paddle(self):
        for position in STARTING_POSITION:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
         
