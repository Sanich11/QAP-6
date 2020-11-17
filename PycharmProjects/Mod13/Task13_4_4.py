"""
    Напишите программу, которая сначала запрашивает логин пользователя, проверяет, существует он или нет,
    а потом с помощью вложенного условия проверяет пароль этого пользователя.
"""

login_list = [
   'root',
   'username1'
   ]

password_list = {
   'root': '1q2w3e4r',
   'username1': 'qwerty123'
   }

username = input('Введите логин:\n')

if username in login_list:
   password = input('Введите пароль:\n')
   if password_list[username] == password:
       print('Вы успешно вошли в систему')
   else:
       print('Отказано в доступе')
else:
   print('Такого пользователя не существует')
