from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

# In the class init we will create the user interface. 
    def __init__(self, quiz_brain: QuizBrain): # Everytime we create a new object from the class QuizInterface, a window will be created
        self.quiz = quiz_brain # quiz_brain: Quizbrain --> When we initialize a QuizInterface we must pass a quiz_brain object
        # which is of the datatype Quizbrain

        self.window = Tk() # We create the window as the property of the class.
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text( 
            150, # The X cordinate, will place the text in the center, as the width is 300
            125, # The Y cordinate, will place the text in the center, as the height is 250
            width=280,
            text="Some question text", 
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="quizzler-app-start/images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="quizzler-app-start/images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop() # This is a kind of while loop that is constantly looking for any change in the app 
# self.window() in this example. So if there is another while loop in the program it will cause problems, so the other
# while loop have to be removed. In this case we have the while loop in the main.py

    def get_next_question(self): # This calls the next question of the list and adds it in the canvas
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled") # This prevents the buttons to be activated
            self.false_button.config(state="disabled")

    def true_pressed(self): # This function does the same than false_pressed, its only using different code.
        self.give_feedback(self.quiz.check_answer("True"))
        
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
