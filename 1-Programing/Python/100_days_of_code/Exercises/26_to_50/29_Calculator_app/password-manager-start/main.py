from tkinter import *
from tkinter import messagebox # Is not a class, etc, so you need to call it because is not included in the asterisk
from random import choice, randint, shuffle  # This way we don't have to type random.shufle() , we only type shufle() and that's it
import pyperclip # You need to install this module. Enables you to copy text to the clipboard

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generator():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for i in range(randint(8, 10))]
    password_symbols = [choice(symbols) for i in range(randint(2, 4))]
    password_numbers = [choice(numbers) for i in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password) # Copies the text (password) to the clipboard, so Crtl + v will have the password.

# ---------------------------- SAVE PASSWORD ------------------------------- #
# This gets into a variable all typed in the 3 entry boxes by separate.
def save():
    website = website_entry.get() # We get what we typed in the entry box and save it into a variable
    email = email_entry.get()
    password = password_entry.get()

    # If we left an entry empty this will warn you. It won't let you to save it until you fill all the boxes
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")

    else: # If all the entry boxes are filled then the else statement will be executed
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} " # This message box appears when you click "Add" and 
                            f"\nPassword {password} \nIs it ok to save? ")# asks you if you whant to cancel (not save the pass, False) or ok (save it, True)
        
        if is_ok: # If you click in OK (True) in the message box this will evaluate to True
            with open("data.txt", mode="a") as file:  # Open data.txt in mode "append" and create the variable "file" to store it's content there.
                file.write(f"{website} | {email} | {password}\n") # Write in data.txt what has been typed in the website box and the email and passwor box too.
                website_entry.delete(0, END) # We delete what is typed in the entry box. Remove from 0 possition to the last one (END), so what you typed in 
                password_entry.delete(0, END) # the box in order to be able to introduce new passwords and user/emails and save them
         
    
# ---------------------------- UI SETUP ------------------------------- # 
# Create the window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50) # We set the padding to x and y

# Create the canvas and call the image
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img) # Create the image inside the canvas. 100 is x and y, so will be in the center of the window
canvas.grid(column=1, row=0) # Use the layout manager grid to place the item in the app window

# LABELS
website_label = Label(text="Website:")
website_label.grid(column=0, row=1,)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# ENTRY
website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()  # Focus the cursor in this entry. So when you run the app the cursor is already in the box.

email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "john@gmail.com") # Insert adds text to the entry box. So in this case will have the email

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")

# BUTTONS
generate_p_button = Button(text="Generate Password", command=password_generator)
generate_p_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()