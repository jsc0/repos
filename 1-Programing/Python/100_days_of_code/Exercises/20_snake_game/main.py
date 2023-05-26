from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)  # We have to turn off the animation. We will use mys_screen.update at the precise place to turn it on when we need.

snake = Snake()
food = Food()
scoreboard = Scoreboard()


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
    
    # Detect collision with food.
    if snake.head.distance(food) < 15:  # if distane is less than 15 it will colide
        food.refresh()
        scoreboard.increase_score()


    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
        
my_screen.exitonclick()