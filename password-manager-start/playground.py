from tkinter import *

def insert_text():
    entry.insert(END, "Hello, World!")

root = Tk()

entry = Entry(root, width=30)
entry.pack()

button = Button(root, text="Insert Text", command=insert_text)
button.pack()

root.mainloop()
