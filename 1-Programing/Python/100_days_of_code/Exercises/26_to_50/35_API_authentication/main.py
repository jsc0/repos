import requests

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "1816fdf74fe2a35c1ee3e87433c3ba47"

weather_parameters = {
"lat": 40.416775,
"lon": -3.703790,
"appid": api_key,
}

# "lat": 55.953251,
# "lon": 3.188267,

response = requests.get(OWN_Endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['list'][:12]

will_rain = False

for i in weather_slice:
    condition_code = i["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:  # We don't put the print statement in the for loop because we don't wan't to print everytime is gonna rain.
    print("Bring an umbrella") # Printing only once the text it's enough, remember that this code checks if is gonna rain in 
                                # the next 12 hours, and if so it will print the message, so you only need to be warned once.

