from turtle import Screen
from snake import Snake
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)  # We have to turn off the animation. We will use mys_screen.update at the precise place to turn it on when we need.

snake = Snake()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    
    snake.move()    

my_screen.exitonclick()