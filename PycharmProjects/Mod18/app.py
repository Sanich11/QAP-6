import telebot


TOKEN = '1419509223:AAElLhdtLugQVBy9KsdBD_lclCj-0i0Lo5g'

bot = telebot.TeleBot(TOKEN)

keys = {
    'рубль': 'RUR',
    'евро': 'EUR',
    'доллар': 'USD',
    'юань': 'CNY',
    'японская иена': 'JPY',
    'фунт стерлингов': 'GBP',
    'гривна': 'UAH',
    'биткоин': 'BTC',
    'эфириум': 'ETH'
}

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу, введите команду боту в следующем формате:\n \
<имя валюты>\n \
<в какую валюту перевести>\n \
<количество переводимой валюты>\n Увидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)

bot.polling()
