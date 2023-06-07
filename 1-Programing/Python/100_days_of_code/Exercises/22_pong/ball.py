from turtle import Turtle

class Ball(Turtle): # Create the class Ball and inherit all methods and attributes from class Turtle

    def __init__(self):  # Declare the init method and create the ball (turtle) shape, color, position, etc
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10  # x cordinate value is 10 now
        self.y_move = 10  # y cordinate value is 10 now

    def move(self): # move the ball (turtle). 
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1  # reverse the numnber, if is possitive turn outs to negative and if negative it became positive.   

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()