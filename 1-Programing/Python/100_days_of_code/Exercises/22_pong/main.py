from turtle import Turtle, Screen
from paddle import Paddle
from paddle import Paddle
import time

PEN_SIZE = 5

# Create the screen and give it size, color and title.
my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("My Pong Game")
# my_screen.tracer(0)

paddle = Paddle()
#paddle.create_paddle()

my_screen.exitonclick()









# # Function to draw a intermitent line.
# def draw_line():
#     for i in range(0, 28):
#         middle_line.pendown()
#         middle_line.forward(10)
#         middle_line.penup()
#         middle_line.forward(10)

# # Draw the center line:
# middle_line = Turtle()
# middle_line.hideturtle()
# middle_line.color("white")
# middle_line.penup()
# middle_line.goto(0, 280)
# middle_line.setheading(270)
# middle_line.pensize(PEN_SIZE)

# draw_line()


