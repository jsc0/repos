from turtle import Turtle

class Ball(Turtle): # Create the class Ball and inherit all methods and attributes from class Turtle

    def __init__(self):  # Declare the init method and create the ball (turtle) shape, color, position, etc
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10  # x cordinate value is 10 now
        self.y_move = 10  # y cordinate value is 10 now
        self.move_speed = 0.1 # The speed the ball will have when is created.

    def move(self): # move the ball (turtle). 
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1  # reverse the numnber, if is possitive turn outs to negative and if negative it became positive.   
        self.move_speed *= 0.9 # Everytime the paddle touches the ball it increases the speed a little.

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9  

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1  # We set the speed to the original one.
        self.bounce_x()