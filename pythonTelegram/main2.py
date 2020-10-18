#pip install python-telegram-bot --upgrade


import telegram

bot = telegram.Bot(token="ffffff")

#print(bot.getMe())

for msg in bot.get_updates() :
    print(msg.message.text)
