"""
Допишите обработчик так, чтобы он из сообщения брал username и выдавал
приветственное сообщение с привязкой к пользователю.
"""


import telebot

TOKEN = "1434023794:AAFFkHW0dci_DusyuVjGYS1YBO3e4CR84tM"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types='text')
def welcome_message(message):
    bot.reply_to(message, f'Приветствую, {message.chat.username}!')
# метод .reply_to() отвечает на сообщение с пересылкой самого сообщения

# ответ с курса
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, f"Welcome, {message.chat.username}")


bot.polling(none_stop=True)
