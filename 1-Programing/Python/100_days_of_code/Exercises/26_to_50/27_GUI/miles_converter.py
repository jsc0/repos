from tkinter import *

def button_clicked():
    operation = float(input.get()) # Get hold of what you are typing
    result = operation * 1.60934
    my_label_result.config(text=result) # When we click the button the text of the label will change

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=150)
window.config(padx=20, pady=20) # Padding. You add more space on the sides

# Entry
input = Entry(width=12)
input.grid(column=2, row=1)

# Label text: Miles
my_label_miles = Label(text="Miles", font=("Arial", 24, "bold" ))
my_label_miles.grid(column=3, row=1)

# Label text: is equal to
my_label_equal = Label(text="is equal to", font=("Arial", 24, "bold" ))
my_label_equal.grid(column=0, row=2)

# Label text: Result converted
my_label_result = Label(text=0, font=("Arial", 24, "bold" ))
my_label_result.grid(column=2, row=2)

# Label text: Km
my_label_km = Label(text="Km", font=("Arial", 24, "bold" ))
my_label_km.grid(column=3, row=2)

# Button    
button = Button(text="Calculate", command=button_clicked) 
button.grid(column=2, row=3)


window.mainloop()