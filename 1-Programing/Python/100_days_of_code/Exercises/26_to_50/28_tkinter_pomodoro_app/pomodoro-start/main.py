from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25   # The program works for 25 minutes
SHORT_BREAK_MIN = 5  # After 25 minutes it goes to a 5 min break
LONG_BREAK_MIN = 20 # The app repeats 4 times, so (25 min work, 5 min break) x4 and then it takes 20 min break
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    root.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    my_label.config(text="Timer")
    my_label_check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM (START TIMER)------------------------------- # 
def start_timer():
    global reps
    reps = 0

    work_sec = WORK_MIN * 60 # We convert the 25 min to seconds, 1500 secs
    short_break_sec = SHORT_BREAK_MIN * 60 # Convert 5 min to seconds, 300 secs
    long_break_sec = LONG_BREAK_MIN * 60 # Convert 20 min to seconds, 1200 secs
    
    if reps % 8 == 0: # 20 min BREAK. If the numbere of breaks divided by 0 has no reminder is time for a long break
        count_down(long_break_sec)
        my_label.config(text="Break", fg=RED)
    elif reps % 2 == 0: # BREAK 5 minutes. If reps is even it's time for a short break
        count_down(short_break_sec)
        my_label.config(text="Break", fg=PINK)
    else:  # If it's none of the previus conditions it's normal work time
        count_down(work_sec)
        my_label.config(text="Work", fg=GREEN)


   

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count): # This function updates the timer display by converting the reminder time  into minutes and seconds
      
    count_min = math.floor(count / 60) # math.floor rounds down to the nearest integer, giving you a whole number of minutes
    count_sec = count % 60

    if count_sec == 0: # Without this will show the seconds with one 0 only instead of two when is necessary, like 25:0 to 25:00
            count_sec = "00"

    # count_sec = f"0{count_sec}" # so we use Dynamic Typing to pass from integer to string.Is just changing the type of the variable.
      
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}" ) #This updates the timer display with the minues and secods. Itemconfig changes a canvas element.
    #And you want to change text="00:00" for the variable count
    

    if count > 0: # If there is remaining time, it schedules the next iteration of the coutdown with 1 second delay.
        global timer
        timer = root.after(1000, count_down, count - 1) # After waits to execute the function x time, 1000 milisecs in this example, which is 1 sec.
    else:
        start_timer() # If count is not greater than 0 the countdown has reached 0 and stat_timer() function is triggered.
        marks = ""
        work_sessions = math.floor(reps/2) # This creates a check mark, ✔, for every 25 minutes. You will have 4 marks and then you will have a 20 min break
        for i in range(work_sessions):
            marks += "✔"
        my_label_check_marks.config(text=marks)

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
button_reset = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
button_reset.grid(row=2, column=2)

# Label check marks
my_label_check_marks = Label(bg=YELLOW, fg=GREEN)
my_label_check_marks.grid(row=3,column=1 )

root.mainloop()