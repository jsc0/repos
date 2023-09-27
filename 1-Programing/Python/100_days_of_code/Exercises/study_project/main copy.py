import tkinter as tk
import pandas as pd
import random

# Set the background color for the app
BACKGROUND_COLOR = "#B1DDC6"

# We use pandas to read the data of the .csv and convert it into a dataframe.
# Then we convert the dataframe to a list of dictionaries. orient="records" means that each row in the DataFrame 
# will be converted into a dictionary, and all these dictionaries will be stored in a list.
data = pd.read_csv("All_in_main_file/data/Questions_Answers.csv").to_dict(orient="records")

# Create separate lists for questions and answers
questions = [row["Question"] for row in data]
answers = [row["Answer"] for row in data]

# Create a function to handle flipping the flashcard
current_card = {"index": 0, "side": "question"}

def flip_card():
    global current_card
    # If currently displaying the question, switch to showing the answer
    if current_card["side"] == "question":
        show_answer()
    else:
        # If currently displaying the answer, switch back to showing the question
        show_question()
    # Toggle the side (question or answer) of the flashcard
    current_card["side"] = "question" if current_card["side"] == "answer" else "answer"

def show_question():
    # Display the question side of the flashcard
    canvas.itemconfig(card_text, text=questions[current_card["index"]])
    canvas.itemconfig(card_background, image=card_front)
    known_button.config(state=tk.NORMAL)

def show_answer():
    # Display the answer side of the flashcard
    canvas.itemconfig(card_text, text=answers[current_card["index"]])
    canvas.itemconfig(card_background, image=card_back)
    known_button.config(state=tk.NORMAL)

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
    text=questions[current_card["index"]],
    width=680,
    font=("Arial", 25)
)

# Create the "Right" button to flip the flashcard
check_image = tk.PhotoImage(file="All_in_main_file/images/right.png")
known_button = tk.Button(image=check_image, highlightthickness=0, command=flip_card)
known_button.grid(row=1, column=0, columnspan=2)

# Start the Tkinter main loop to run the app
window.mainloop()
