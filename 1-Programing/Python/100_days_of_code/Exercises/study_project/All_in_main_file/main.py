import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# This gets you the data of the .csv, it converts it to a dataframe, then converts it to a list of dictionaries
data = pd.read_csv("All_in_main_file/data/Questions_Answers.csv").to_dict(orient="records")

current_card = {"index": None, "side": "question"}

# This code defines a function called get_show_question() that, when called, selects 
# a random question from a list of questions (stored in the data variable), 
# sets the current side to "question", and then displays the selected question on the screen.
def get_show_question():
    global current_card
    current_card["index"] = random.randint(0, len(data) - 1)
    current_card["side"] = "question"
    show_question()

# Function to flip the flashcard between question and answer
def flip_card():
    global current_card
    if current_card["index"] is not None:
        if current_card["side"] == "question":
            show_answer()
        else:
            show_question()

# Function to display the question side of the flashcard
def show_question():
    global current_card
    if current_card["index"] is not None:
        canvas.itemconfig(card_text, text=data[current_card["index"]]["Question"])
        canvas.itemconfig(card_background, image=card_front)
        current_card["side"] = "question"

# Function to display the answer side of the flashcard with each line on a new line
def show_answer():
    global current_card
    if current_card["index"] is not None:
        answer_text = str(data[current_card["index"]]["Answer"]).replace('\\n', '\n')
        wrapped_text = "\n".join(answer_text.split('\n'))  # Split by '\n' and join with '\n' again
        canvas.itemconfig(card_text, text=wrapped_text)
        canvas.itemconfig(card_background, image=card_back)
        current_card["side"] = "answer"

# Create the Tkinter window
window = tk.Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# Create the canvas to display flashcards
canvas = tk.Canvas(height=526, width=800, background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Load card images for the front and back of the flashcard
card_front = tk.PhotoImage(file="All_in_main_file/images/card_front.png")
card_back = tk.PhotoImage(file="All_in_main_file/images/card_back.png")

# Create the initial flashcard with a question side
card_background = canvas.create_image(0, 0, anchor="nw", image=card_front)
card_text = canvas.create_text(
    400, 200,
    fill="black",
    text="",
    width=680,
    font=("Arial", 25)
)

# Create the Answer/Question button to flip the flashcard
known_button = tk.Button(text="Answer/Question", highlightthickness=0, width=15, height=2, command=flip_card)
known_button.grid(row=1, column=0)

# Create the Next Question button
next_question_button = tk.Button(text="Next Question", highlightthickness=0, width=15, height=2, command=get_show_question)
next_question_button.grid(row=1, column=1)

# Automatically show the first question when the app starts
get_show_question()

# Start the Tkinter main loop to run the app
window.mainloop()
