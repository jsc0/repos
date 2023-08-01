from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- Functions ------------------------------- #
data = pandas.read_csv("data/french_words.csv") # We use pandas to get the data from the csv. So convert the .csv into a pandas dataframe
to_learn = data.to_dict(orient="records") # We convert the dataframe into a lot of dictionaries inside a list, orient=records does that, convert it in the proper way

current_card = {} # We will store the random choiced dictionary here.

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer) # If you press the button that triggers this function several times after_cancel

    current_card = random.choice(to_learn) # Get a random dictionary, remember "to_learn" contains this [{'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'}, ...
    canvas.itemconfig(card_title, text="French", fill="black" ) # Change the text of card_title variable (see Labels section below)
    canvas.itemconfig(card_word, text=current_card["French"], fill="black") # Change the text in the label to show the VALUE of the key French randomly choosen and change the text to black color
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card) ################## This calls the function after 3 seconds

def flip_card(): # We change the words to English and we show the english word
    canvas.itemconfig(card_title, text="English", fill="white") # fill means that we change the color of the text to white
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    next_card()
    data.to_csv("data/words_to_learn.csv")
# ---------------------------- UI SETUP ------------------------------- #

# Create the Window from Tkinter
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card) ################## This calls the function after 3 seconds the first time we run the program

# Canvas. We remove the borders (edges) and add the same color of the background color.
canvas = Canvas(height=526, width=800, background=BACKGROUND_COLOR, highlightthickness=0)

## Load the images
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

## Add the image to the canvas. THIS SHOWS THE WHITE IMAGE
card_background = canvas.create_image(0, 0, anchor="nw", image=card_front)
 
# LABELS (text) to the Canvas
card_title = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic")) # We leave empty the text="" because the text will be filled by 
card_word = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold")) # the random word choosen by next_card() function

canvas.grid(row=0, column=0, columnspan=2)

# Buttons. THEY CALL THE FUNCTION next_card()
wrong_button_image = PhotoImage(file="images/wrong.png") # We create the image
wrong_button = Button(image=wrong_button_image, command=is_known) # We assign the image inside the button and when we press the button will runs next_card() function
wrong_button.grid(row=1,column=0)

right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, command=next_card) # When we press the button will runs next_card() function
right_button.grid(row=1, column=1)

# -------------------- Next Card Function --------------------------------- #
next_card() # We call the function to pick randomly a french word that will appear when you run the app



window.mainloop()

