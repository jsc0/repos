from tkinter import *

def button_countdown(i, puta):
    if i > 0:
        i -= 1
        minutes = i // 60
        seconds = i % 60
        polla = f"{minutes}:{seconds}"
        puta.set(polla)
        root.after(1000, button_countdown, i, puta) # Tell button_countown to wait 1 second (1000 milisecs) before running again. pass in 1 and label too.
    else:
        close()

def close():
    root.destroy()

root = Tk()

counter = 1500
button_label = StringVar()
button_label.set(counter)
Button(root, textvariable=button_label, command=close).pack()
button_countdown(counter, button_label)

root.mainloop()
