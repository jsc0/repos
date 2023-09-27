from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try: # words_to_learn.csv doesn't exist. Is created when you press the green button for the fist time, until then 
    data = pandas.read_csv("Solution+-+flash-card-project-end/data/words_to_learn.csv") # the "try" will fail and will jump to the exeption.
except FileNotFoundError: # This exeption will create a dataframe from the csv, and will be converted into a list.
    original_data = pandas.read_csv("Solution+-+flash-card-project-end/data/french_words.csv")# Pandas read the .csv
    print(f"printing original data {original_data}") # We print it for learning purposes
    to_learn = original_data.to_dict(orient="records")# We convert the dataframe to a list (to_learn)
else:
    to_learn = data.to_dict(orient="records") 


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known(): # When we press the known_button we trigger this function.
    to_learn.remove(current_card) # Which removes the current card from the list "to_learn"
    print(len(to_learn)) # This is just to show in the cli that we remove a word from the list.
    data = pandas.DataFrame(to_learn) # We create a dataframe from to_learn, which has a word less removed in the previous step
    data.to_csv("data/words_to_learn.csv", index=False) # We create the new .csv with the dataframe with the word removed. Index false is to not save the index number
    next_card() # and we call the next_card() function 


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()



