import Constants as keys
from telegram.ext import *
import Responses as R

print("bot started...")


def start_message(update, context):
    update.message.reply_text("Please write the name of any Cryptocurrency")


def help_message(update, context):
    update.message.reply_text("Google it!")


def handle_message(update, context):
    text = str(update.message.text)
    response = R.sample_responses(text)
    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_message))
    dp.add_handler(CommandHandler("help", help_message))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
