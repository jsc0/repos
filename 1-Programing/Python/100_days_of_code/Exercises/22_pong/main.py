from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Create the screen and give it size, color and title.
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)  # --> Turn off the animation. Then the right_paddle gets created and we update the image after it.

# Initialize Right and Left paddles from Paddle class and pass in starting positions in a Tuple
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# We initialize ball from Ball class. Ball inherits methods and attributes from Turtle class.
ball = Ball()

scoreboard = Scoreboard()

# Enable screen listening to detect the keys you press and run the methods go_up or go_down if you press the arrows up and down or w or s.
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# To update the image, "tracer" disable the animation and "update" method shows a picture of the current image.
game_is_on = True
while game_is_on:
    time.sleep(0.1) # We slow the screen because the ball goes too fast
    screen.update() # Update the screen, is like to show a picture of the screen in every iteration of the while loop.
    ball.move()  # We got the ball to move with every refresh of the screen.

# Detect collision with top wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()  # it detects when the ball hits the top or bottom of the screen.

# Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

# Detect when R paddle misses:
    if ball.xcor() > 380:
        ball.reset_position() 
        scoreboard.l_point()      
        
# Detect when L paddle misses:
    if ball.xcor() < - 380:
        ball.reset_position() 
        scoreboard.r_point()   

screen.exitonclick()