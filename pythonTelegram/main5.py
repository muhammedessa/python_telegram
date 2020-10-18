#option

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

updater = Updater(token="fffffffff")
dispatcher = updater.dispatcher

def option(bot, update):
    button = [
        [InlineKeyboardButton("Muhammed Essa", callback_data="Muhammed Essa"),
         InlineKeyboardButton("Ahmed Essa", callback_data="Ahmed Essa")],
        [InlineKeyboardButton("Osama Essa", callback_data="Osama Essa")]
    ]
    reply_markup = InlineKeyboardMarkup(button)

    bot.send_message(chat_id=update.message.chat_id,
                     text="Click anyone",
                     reply_markup=reply_markup)


option_handler = CommandHandler("option", option)
dispatcher.add_handler(option_handler)


def button(bot, update):
    querydata = update.callback_query
    bot.send_message(chat_id=querydata.message.chat_id,
                     text="You select {}.".format(querydata.data))


button_handler = CallbackQueryHandler(button)
dispatcher.add_handler(button_handler)
updater.start_polling()
