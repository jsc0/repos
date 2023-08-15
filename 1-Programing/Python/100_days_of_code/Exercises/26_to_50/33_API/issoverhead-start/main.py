import requests
from datetime import datetime
import smtplib

MY_LAT = 55.953251 # Your latitude
MY_LONG = -3.188267 # Your longitude

my_email = "test.1980.joder@gmail.com"
password = "extujufevmdguvmq"

# Get me the possition of the ISS
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# If your position is within +5 or -5 degrees of the ISS position
# and is sunset in your location then send me an email informing me about it.
# If not will print a message saying is still soon
if int(iss_latitude) in range(50, 60) and int(iss_longitude) in range(2, -9, -1):

    # Get me the sunrise/sunshine in my city
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status() # If any, show me the code error
    data = response.json() # Convert the data received to a python dictionary
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) # Get me the hour only
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) # Get me the hour only

    time_now = datetime.now()
    hour = time_now.hour

    # Checks if it's dark, if so will send an email informing that the ISS is passing over your head
    if hour >= sunset or hour <= sunrise: 
        print("Ullet")
        with smtplib.SMTP("smtp.gmail.com") as connection: # We create the connection
            connection.starttls() # To secure our connection to the email server
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs="cuenta.fact10@gmail.com", 
                msg="Subject:Hello fuker\n\nThe International Space Station is passing over your head, take a look."
            )
    else:
        print("The ISS is passing over you but is not dark yet")

else:
    print("The ISS is still far from your sky")


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds if the ISS is overhead.



