import logging
from telegram.ext import *
import responses

from config import API_ID, API_HASH, BOT_TOKEN

bot=Client(
     "Pyrogram Bot", 
     bot_token=os.environ["BOT_TOKEN"],
     api_id=int(os.environ["API_ID"]), 
     api_hash=os.environ["API_HASH"],
) 


# Set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s %(message)s', level=logging.INFO)
logging.info('Starting Bot...')


def start_command(update, context):
    update.message.reply_text('https://te.legra.ph/file/e719f19bbeeb7f55e6202.jpg '
                              'hello iam chat bot deployed on python server deployed by: @santhu_music_bot')




def help_command(update, context):
    update.message.reply_text('Try typing anything and I will do my best to respond!')



def custom_command(update, context):
    update.message.reply_text('This is a custom command, you can add whatever text you want here.')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = responses.get_response(text)
    logging.info(f'user ({update.message.chat.id}) says: {text}')

    # Bot response
    update.message.reply_text(response)


def error(update, context):
    # Logs errors
    logging.error(f'update {update} caused error {context.error}')


if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)
    
    
    bot.run()
