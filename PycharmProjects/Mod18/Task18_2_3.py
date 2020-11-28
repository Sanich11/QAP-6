"""
Напишите программу, которая отправляет запрос на генерацию случайных текстов (используйте этот сервис -
https://baconipsum.com/api/). Выведите первый из сгенерированных текстов.
"""

import requests
import json

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')

r = json.loads(r.content)
# делаем из полученных байтов python объект для удобной работы

print(type(r))
print(r[0])
