from datetime import datetime 
import pandas
import random
import smtplib


today = datetime.now()
today_tuple = (datetime.now().month, datetime.now().day) # We create the tuple with today's month and day, like (12,30)

# Use pandas to read the birthdays.csv
data = pandas.read_csv("birthdays.csv")

# Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
# Dictionary comprehension for pandas DataFrame looks like this: So iterate all the values in all rows (data.interrows) one by one.
# you get the index and the values of each row (data_row), the values in each row is (John test@email.com  1961  7 26)
# Then you get the column month value and the column day value and you store it in a tuple (month, day) --> this is gona be the new_key (keyword terminology)
# the value will be the whole row (John test@email.com  1961  7 26), and you will be storing this in the new dictionary.
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24

#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

# Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if today_tuple in birthdays_dict: # If the today mondy and day in inside birday_dict then
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt" # Choose one of the letters
    birth_person = birthdays_dict[today_tuple] # We get hold of the values that contains the key today_tuple, which is a day and month, like (21, 7)
    with open(file_path) as letter_file: # We open the letter.txt randomly selected before
        contents = letter_file.read() # We read it
        contents = contents.replace("[NAME]", birth_person["name"])  # Replace the literal [NAME] for the value of the key 'name'
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="IN_PASS_PLACEr@gmail.com", password="IN_PASS_PLACE")
        connection.sendmail(
            from_addr="test.1980.joder@gmail.com",
            to_addrs=birth_person["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}"   
        )