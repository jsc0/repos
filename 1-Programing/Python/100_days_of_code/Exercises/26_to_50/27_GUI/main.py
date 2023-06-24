from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get() # Get hold of what you are typing
    my_label.config(text=new_text) # When we click the button the text of the label will change

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20) # Padding. You add more space on the sides

# Label
my_label = Label(text="New Text", font=("Arial", 24, "bold" ))
my_label.grid(column=0, row=0)

# Button    
button = Button(text="Click Me", command=button_clicked) 
button.grid(column=1, row=1)

# New Button    
new_button = Button(text="Click Me New Button", command=button_clicked) 
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)



window.mainloop()

