from telegram import Bot
from telegram.ext import Updater, CommandHandler
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="أهلاً بك! البوت شغال.")

def notify(update, context):
    context.bot.send_message(chat_id=CHANNEL_ID, text="تنبيه من أبو فيصل الملكي")

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('notify', notify))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
