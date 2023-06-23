import tkinter

# Window is like the screen in turtle module
window = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I Am a label", font=("Arial", 24, "bold" ))

# You have to use .pack() to make appear the label into the screen
#my_label.pack(side="left")
my_label.pack(expand=True)

# Loop to keep the window running, like exitonclic() in the screen class
window.mainloop()

# This is the same loop than the mainloop() method
# while True:
#     listening
