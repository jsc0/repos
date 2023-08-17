import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "___YOUR_EMAIL_HERE____"
MY_PASSWORD = "___YOUR_PASSWORD_HERE___"
MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

# Checks if the ISS is over your sky, if so return True
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json") # Get me the data from the API
    response.raise_for_status() # If error show me the code number.
    data = response.json() # Convert the data to a dictionary to help python to handle the data

    iss_latitude = float(data["iss_position"]["latitude"]) # Sort the data to get only the latitude
    iss_longitude = float(data["iss_position"]["longitude"]) # Sort the data to get only the longitude

    # Check if my sky lat/long is the same than the ISS position +5 or -5 degrees of the iss position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

# Checks if we are in the night, if so returns True
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) # This gets you an int like 19 that
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) #  has to be between 00 and 23 hours 

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

# While the two functions are True send an email. This code will wait 60 seconds and 
# will check again if the two conditions are still true.
# The ISS would be over your sky only for 2 or 3 minutes so you should
# receive only 2 or 3 emails

while True:
    time.sleep(60) # Run this block every 60 seconds
    if is_iss_overhead() and is_night(): # If both functions are true send the email
        connection = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )


