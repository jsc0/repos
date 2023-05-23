from turtle import Turtle, Screen
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)  # We have to turn off the animation. We will use mys_scree.update at the precise place to turn it on when we need.

starting_position = [(0, 0 ), (-20, 0), (-40, 0)]

segments = []

# Creates 3 instances/objects, adds shape, color, and more stuff and stores them into a list.
for position in starting_position:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# Move the snake.
game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num -1].xcor()
        new_y = segments[seg_num -1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)



my_screen.exitonclick()