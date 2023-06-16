from turtle import Turtle

VERTICAL = 5
HORIZONTAL = 1

# We create the Paddle class and we inherit the class Turtle, so now we have all the methods and attributes from turtle plus the ones we create for Paddle.
class Paddle(Turtle):
    
# We declare the init method providing the spects that the paddle (turtle) will have and where is gonna be located.
    def __init__(self,starting_position): # We pass in x and y cordinades
        super().__init__()  #  --> To use Class Inherit we need to call it like this.
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(VERTICAL, HORIZONTAL)
        self.goto(starting_position)  # We pass in the cordinades that we want (left or right paddle). 

# Method go_up will move the paddle (turtle) up +20. We retrieve where the y and x cords are, we add +20 to y cord and we move the paddle to the new possition
    def go_up(self):  # We create the method go_up. ycor and xcor methods just says the current position of the turtle, y = vertical, x = horizontal
        new_y = self.ycor() + 20  # ycor says the possition where the turtle is and we add +20 pixels to that possition.
        self.goto(self.xcor(), new_y) # We ask to the turtle to move to the x cordinates (which is always 0) and the y cordinates wich is old ycord +20

    def go_down(self):
        new_y = self.ycor() - 20  
        self.goto(self.xcor(), new_y)
