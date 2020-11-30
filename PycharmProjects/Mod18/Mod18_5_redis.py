import redis
import json

# обязательная часть
red = redis.Redis(
    host='redis-19047.c98.us-east-1-4.ec2.cloud.redislabs.com',
    port=19047,
    password='pZkczWmQuoB5VhqwqvKJapuotP2cUvyz'
)

red.set('var', 'value') # записываем в кэш строку "value"
print(red.get('var')) # считываем из кэша данные


dict1 = {'key1': 'value1', 'key2': 'value2'} # создаём словарь для записи

# с помощью функции dumps() из модуля json превратим наш словарь в строчку
red.set('dict1', json.dumps(dict1))

# с помощью функции loads превращаем данные полученные из кэша обратно в словарь
converted_dict = json.loads(red.get('dict1'))

print(type(converted_dict)) # убеждаемся, что получили действительно словарь
print(converted_dict) # ну и выводим его содержание

# red.delete('dict1') # удаляются ключи с помощью метода .delete()
# print(red.get('dict1'))
