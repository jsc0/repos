# This code get you the questions and all the info related to it via API from a trivia website.
# We pass in the parameters to the API's website, in this example we want to receive
# 10 questions with bolean answer True/False (the other option would be multiple choice answer).

# You will receive a json with info like this:
# {"response_code":0,"results":[{"category":"Entertainment: Cartoon & Animations","type":"boolean","difficulty":"easy",
#"question":"In the &quot;Shrek&quot; film franchise, Donkey is played by Eddie Murphy.
# ","correct_answer":"True","incorrect_answers":["False"]} ...

# Then we enable to be show any error code if any, then will convert the data received to 
# a dictionary for python to be able to handle it.

# And we sort the data received to have only the questions and info related to it skiping other non related 
# info like the response code of the beggining.

# question_data, which is a dictionary that will look like this:
# [{'category': 'Science: Computers', 'type': 'boolean', 'difficulty': 'medium', 'question': 
# 'The HTML5 standard was published in 2014.', 'correct_answer': 'True', 'incorrect_answers': ['False']}, 

# question_data will be called from main.py and there the information will be sorted more specifically
import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]

# How to modify the questions you receive:
# Add a new parameter:
#   "category": 18,  --> which is to get only computing stuff questions. Check the website to use the category you want
# This is the whole url:  https://opentdb.com/api.php?amount=10&category=18&type=boolean