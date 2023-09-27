# This program get's the stock price of tesla, filters the last two closing prices, so yesterday and two days ago closing price
# Then compares both prices and gets the difference and gives you the % that have changed, example: 
# closing price 2 days ago =  100, closing price yesterday = 90, difference 10, the price have decreased 10%
# If the price goes up or down 5% you will receive an sms informing about this and will give you 
# the 3 first news of the company that may explain the price raise/down.

import requests
import os
from twilio.rest import Client

# STOCK API CONSTANTS
STOCK_NAME = "TSLA"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
APIKEY = "O3DSNIEU069TTL92"
# APIKEY = os.environ.get("STOCKS_API_KEY")    # The API has been saved as environment variable by exporting it through the terminal, name: STOCKS_API_KEY

# STOCKS API PARAMETERS: To pass in to the stocks API
parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":"APIKEY",
}

# Get the STOCK data from the API
response = requests.get(STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"] # We convert the data to json and we save only the key of Time Series.. (which contains a lot of dictionaries)

# Convert the data received, which is a lot of dictionaries within a dictionary (json format), to a LIST of dictionaries to be able to retrieve it's content using idexes.
data_list = [value for (key, value) in stock_data.items()] # .items() is a function that gets you each key:value from the dictionary

# Example, if I print(data_list) I got a list that contains a lot of dictionaries inside, see below:
# [{'1. open': '251.2200', '2. high': '256.5200', '3. low': '246.6700', '4. close': '248.5000', '5. volume': '118559635'}, {'1. open': '245.0700'...

# Now I can use indexes to search for a particular value:key --> stock_data[0]["2. high"] --> '256.5200'

# Let's get the closing price of the stock from yesterday and two days ago
yesterday_closing = float(data_list[0]["4. close"]) # We get the price from yesterday [0] (0 is the first possition in the list).
before_yesterday_closing = float(data_list[1]["4. close"]) # Here we get the closing price from 2 days ago, as [1] is the second item on the list

# We substract both prices and we make the value positive with abs, because we need it positive to calculate the % in the next step
positive_difference = abs(yesterday_closing  - before_yesterday_closing) 

# We calculate how much % the price of the stock have increased or decreased, we calculate using after yesterday closing price
percentage = float(format((positive_difference / before_yesterday_closing) * 100, ".2f")) # .2f gets you the first two digits after the dot, like 3.45
# instead of getting the full number, 3.45654564564

# We create the SIGNS Constants
SIGN_UP = "🔺"
SIGN_DOWN = "🔻"
SIGN = ""

# This will print (or send via sms) the sing up or down depending on the comparation of the closing prices, check the end of this file to 
# see the format the SMS will have to understad this.

if yesterday_closing > before_yesterday_closing: # If the price is higer yesteday it will have the SIGN_UP sign and the oposite if not
    SIGN = SIGN_UP
else:
    SIGN = SIGN_DOWN

# NEWS API: Get the first 3 news from the company

######### STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# NEWS API CONSTANTS
COMPANY_NAME = "tesla"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_APIKEY = "65769c9ac1e644baa8492a90647915b2"

# NEWS API PARAMETERS
parameters_news = {
    "q":COMPANY_NAME,
    "sortBy":"publishedAt",
    "language":"en",
    "apiKey":NEWS_APIKEY
}

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

# Get NEWS from the API
response_news = requests.get(NEWS_ENDPOINT, params=parameters_news)
response_news.raise_for_status()
news_data = response_news.json()["articles"][:3] # Get the last 3 articles

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# Get the title (headline) of the 3 news selected before and add in into a list.
headlines = [news_data[i]["title"] for i in range(3)]

######### STEP 3: Use twilio.com/docs/sms/quickstart/python to send a separate message with each article's title 
# and description to your phone number. 

# auth_token = os.environ["TWILLIO_AUTH_TOKEN"]   ---> The envar are in ~/.zshrc but when run "env" does not appear there,
# account_sid = os.environ.get["TWILLIO_ACCOUNT_SID"]  ---> check what is going on

account_sid = "AC33603b685941919d0698cca18589eaa5"
auth_token = "f7ed2f19d885a048aa2a94dff7997740"


def Send_SMS(message):
    OJETE = f"TSLA: {SIGN} {percentage}% \n{message}"
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
                body=OJETE,
                from_="+447883316445",
                to="+447593311922"
                )
    print(message.sid)
    print(OJETE)

for i in headlines:
    Send_SMS(i)

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

