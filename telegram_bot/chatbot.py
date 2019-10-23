import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token = "620472562:AAENVcmTsxZZSCA_5boE2QBTeLWaTKt6nI4"
bot = telegram.Bot(token = token)
def get_message(bot, update):
    update.message.reply_text(update.message.text)
def get_whatyourname(bot, update):
    update.message.reply_text("HeonJin Jeong")
updater = Updater(token)
commanderhandler = CommandHandler("name", get_whatyourname)
updater.dispatcher.add_handler((commanderhandler))
messagehandler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(messagehandler)

updater.start_polling(timeout=10, clean=True)
updater.idle()
