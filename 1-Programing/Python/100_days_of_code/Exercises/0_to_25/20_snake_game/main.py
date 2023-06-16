from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Use the class Screen from the turtle method to provide the size, background color, title, etc of the screen.
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)  # We have to turn off the animation. We will use mys_screen.update at the precise place to turn it on when we need.

# Create the objects (instances) from the proper classes.
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Enable the screen to detect when you press a key.
my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")

# PROGRAM STARTS:
game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()    
    
    # Detect collision with food.
    if snake.head.distance(food) < 15:  # if distane is less than 15 it will colide
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail. If head collides with any segment in the tail trigger game_over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    
        
my_screen.exitonclick()