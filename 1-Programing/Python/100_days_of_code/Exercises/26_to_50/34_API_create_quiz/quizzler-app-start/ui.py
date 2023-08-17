from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

# In the class init we will create the user interface. 
    def __init__(self): # Everytime we create a new object from the class QuizInterface, a window will be created
        self.window = Tk() # We create the window as the property of the class.
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text( 
            150, 
            125, 
            text="Some question text", 
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop() # This is a kind of while loop that is constantly looking for any change in the app 
# self.window() in this example. So if there is another while loop in the program it will cause problems, so the other
# while loop have to be removed. In this case we have the while loop in the main.py