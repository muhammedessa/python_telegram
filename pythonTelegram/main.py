# pip install requests
#
# https://api.telegram.org/bot<token>/getUpdates
#
# https://github.com/python-telegram-bot/python-telegram-bot
















import requests

from pprint import pprint

url = "https://api.telegram.org/bot<token>/getUpdates"

response = requests.get(url)

# pprint(response.json())


# for msg in response.json()['result'] :
#     pprint(msg['message']['text'])

