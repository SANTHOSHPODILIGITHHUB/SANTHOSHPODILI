import telegram bot
import ext. telegram
START_MESSAGE = "nenu simple chat bot ni made with python server deploy by: @santhu_music_bot",
START_MESSAGE_BUTTONS = [
    [InlineKeyboardButton('NETWORK', url='https://t.me/santhuvc')]
]

@bot.on_message(filters.command('start') & filters.private)
def start(bot, message):
    text = START_MESSAGE




    reply_markup = InlineKeyboardMarkup(START_MESSAGE_BUTTONS)
    message.replyI(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )
    @bot.on_message(filters.command('help'))
    def command2(bot, messager):
        message.reply_text("This is santhu bot's help section.")






"
