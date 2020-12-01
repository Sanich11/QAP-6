"""
Напишите программу, которая будет записывать и кэшировать номера ваших друзей. Программа должна уметь воспринимать
несколько команд: записать номер, показать номер друга в консоли при вводе имени или же удалить номер друга по имени.
Кэширование надо производить с помощью Redis. Ввод и вывод информации должен быть реализован через консоль
(с помощью функций input() и print()).
"""


import redis


red = redis.Redis(
    host='redis-19047.c98.us-east-1-4.ec2.cloud.redislabs.com',
    port=19047,
    password='pZkczWmQuoB5VhqwqvKJapuotP2cUvyz'
)


counter = True

while counter:
    action = input('Введите действие (write, read, delete):\t')
    if action == 'write':
        name = input('Введите имя:\t')
        phone = input('Введите номер:\t')
        red.set(name, phone)
    elif action == 'read':
        name = input('Введите имя:\t')
        phone = red.get(name)
        if phone:
            print(f'Номер {name}: {str(phone)}')
        else:
            print(f'Имя {name} не найдено')
    elif action == 'delete':
        name = input('Введите имя:\t')
        phone = red.delete(name)
        if phone:
            print(f'Номер {name} удалён')
        else:
            print(f'Имя {name} не найдено')
    elif action == 'stop':
        print('Всего доброго!')
        break
