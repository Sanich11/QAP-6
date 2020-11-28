"""
Напишите обработчик, который на сообщения с фотографией будет отвечать сообщением «Nice meme XDD».
Бот должен отвечать не отдельным сообщением, а с привязкой к картинке.
"""


import telebot

TOKEN = "1434023794:AAFFkHW0dci_DusyuVjGYS1YBO3e4CR84tM"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['photo'])
def answer_photo(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')


bot.polling(none_stop=True)
