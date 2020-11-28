import telebot

TOKEN = "1434023794:AAFFkHW0dci_DusyuVjGYS1YBO3e4CR84tM"

bot = telebot.TeleBot(TOKEN)  # создание объекта bot

# Параметр none_stop=True говорит, что бот должен стараться
# не прекращать работу при возникновении каких-либо ошибок.


@bot.message_handler(content_types='text')  # декоратор - Обработчик сообщений
def repeat(message: telebot.types.Message):
    bot.send_message(message.chat.id, "This is a message handler")


bot.polling(none_stop=True)  # запуск бота


# # Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
# @bot.message_handler(commands=['start', 'help'])
# def handle_start_help(message):
#     pass
#
#
# # Обрабатывается все документы и аудиозаписи
# @bot.message_handler(content_types=['document', 'audio'])
# def handle_docs_audio(message):
#     pass
