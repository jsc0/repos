from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):

    def __init__(self):  # Constructor method.Initializes the attributes of the Scoreboard object, color, pen,etc.
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard() # We call this method to initialy display the scores.

# We create a separated function to update the scoreboard. We could leave all in the constructor method 
# but by Single Responsibility Principle we should use the constructor to generate the object only 
# and update_scoreboard to update the score. All methods should be doing only one task by its own 
# function promoting code organization, reusability, readability, and maintainability
    def update_scoreboard(self): 
        self.clear()  # We need to clear the screen everytime, otherwise the numbers will appear on top of the 
        #last one.0, 1, 2, etc on top of each other
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()