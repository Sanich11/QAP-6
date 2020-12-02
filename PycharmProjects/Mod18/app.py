import telebot
from config import keys, TOKEN
from extensions import ConvertionException, Cryptoconverter


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])  # обработчик команд start и help
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу, введите команду боту в следующем формате:\n \
<имя валюты>\n \
<в какую валюту перевести>\n \
<количество переводимой валюты>\n Увидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])  # обработчик команды values - какие валюты доступны
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])  # обработчик конвертации валют
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:  # проверяем, что пользователь ввёл не более трёх необходимых параметров
            raise ConvertionException('Неверное количество параметров')

        quote, base, amount = values
        total_base = Cryptoconverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя \n {e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду \n {e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'  # итоговый вывод конвертации
        bot.send_message(message.chat.id, text)


bot.polling()
