import telebot
bot = telebot.TeleBot('t o k k e n')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'КУ-КУ )')
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 're: ' + message.text + ' <= не пиши мне такое')
bot.polling(none_stop=True, interval=0)
