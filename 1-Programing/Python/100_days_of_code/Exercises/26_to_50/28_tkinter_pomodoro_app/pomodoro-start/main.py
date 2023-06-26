from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    print("Reset Button")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps = 0

    work_sec = WORK_MIN * 60 
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        my_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        my_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        my_label.config(text="Work", fg=GREEN)


    # count_down(1500)  # We call the method that will show the count down into the tomato label

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
      
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0:
            count_sec = "00"

    # elif count_sec < 0:   # Without this will show the seconds with one 0 only instead of two when is necessary, like 25:0 to 25:00
    #         count_sec = f"0{count_sec}" # so we use Dynamic Typing to pass from integer to string.Is just changing the type of the variable.
      
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}" ) # itemconfig changes a canvas element. And you want to change text="00:00" for the variable count
    if count > 0:
        root.after(1000, count_down, count - 1)
    else:
         start_timer()


# ---------------------------- UI SETUP ------------------------------- #
# Use Tkinter to create a new window, run it and put a background color
root = Tk()
root.title("Pomodoro")
root.config(padx=100, pady=50, bg=YELLOW)

# We create the canvas (lienzo). We 
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) # We create object canvas, highligh.. --> remove the edges
tomato_img = PhotoImage(file="tomato.png") # We create the image and store it in tomato_img
canvas.create_image(100, 112, image=tomato_img)  # You need the x and y possition of the image on the canvas.
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")) # The text. This is the count down numbers.
canvas.grid(row=1, column=1)

#Label Timer
my_label = Label(text="Timer", bg=YELLOW, fg=GREEN,font=(FONT_NAME, 50) )
my_label.grid(row=0, column=1)

#Button Start
button_start = Button(text="Start", highlightbackground=YELLOW, command=start_timer) 
button_start.grid(row=2, column=0) 

#Button Reset
button_reset = Button(text="Reset", highlightbackground=YELLOW, command=reset)
button_reset.grid(row=2, column=2)

# Label check marks
my_label_check_marks = Label(text="✓", bg=YELLOW, fg=GREEN)
my_label_check_marks.grid(row=3,column=1 )

root.mainloop()