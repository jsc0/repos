import requests
from twilio.rest import Client
import os

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWN_API_KEY")
account_sid = "AC33603b685941919d0698cca18589eaa5"
auth_token = os.environ.get("AUTH_TOKEN")

weather_parameters = {
"lat": 37.983810,
"lon": 23.727539,
"appid": api_key,
}

response = requests.get(OWN_Endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['list'][:12] # This filters the first 12 results from the API

will_rain = False

# Now we filter the info and we get only the meteorigical condition code, which tells you if rains, snows, etc
for i in weather_slice:
    condition_code = i["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain: # Send an SMS if the will_rain is True
    client = Client(account_sid, auth_token) # We set up the twilio client
    message = client.messages.create(
        from_="+447883316445", # The sender of the SMS, phone number created by twilio
        body="It's going to rain today. Remember to bring an umbrella.",
        to="+447593311922" # The receptionist of the sms    
    )
    print(message.status)