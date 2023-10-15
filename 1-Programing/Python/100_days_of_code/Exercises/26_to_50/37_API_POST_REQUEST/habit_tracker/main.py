# Habit tracking project using Pixela. 

import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token" : "asdfasdfadsfadsf23423@£@£$!", # Yoy create the token, which is like the APIKEY
    "username" : "my_username_jsc",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

requests.post(url=pixela_endpoint, json=user_parameters) # We use json parameter because we are POSTing data (user_parameters) which is in json format basically
