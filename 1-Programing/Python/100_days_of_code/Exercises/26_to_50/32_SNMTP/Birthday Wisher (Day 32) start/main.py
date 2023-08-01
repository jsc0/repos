import datetime as dt
import smtplib
from random import choice

CORRECT_DAY = "Friday"

# CONVERT THE DATA: From .txt to a list
with open("quotes.txt") as data:
    list_quotes = data.readlines()

# GET THE FULL NAME OF THE DAY WE ARE IN
now = dt.datetime.now() # Create the object "now" with the class datetime.
day = now.strftime('%A') # We get the full name of the day of the week we are in

if CORRECT_DAY == day:
    quote = choice(list_quotes)


my_email = "test.1980.joder@gmail.com"
password = "extujufevmdguvmq" # The app password created in gmail - security -- app 

with smtplib.SMTP("smtp.gmail.com") as connection: # We create the connection
    connection.starttls() # To secure our connection to the email server
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="1900_receiving_acccount@proton.me", 
        msg=f"Subject:Quote of the week\n\n{quote}"
    )