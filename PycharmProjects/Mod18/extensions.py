import requests
import json
from config import keys


class ConvertionException(Exception):  # создали свой класс обработки исключений (ошибок ввода)
    pass


class Cryptoconverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:  # проверка на ввод двух одинаковых валют - не конвертируем из себя в себя
            raise ConvertionException('Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:  # если не правильно ввели валюту, из которой конвертируем
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:  # если не правильно ввели валюту, в которую конвертируем
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:  # проверка, что количество валюты ввели цифрами
            raise ConvertionException(f'Не удалось обработать количество {amount}')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base
