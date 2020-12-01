import telebot


TOKEN = '1419509223:AAElLhdtLugQVBy9KsdBD_lclCj-0i0Lo5g'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler()
def echo_test(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'hello')


bot.polling()
