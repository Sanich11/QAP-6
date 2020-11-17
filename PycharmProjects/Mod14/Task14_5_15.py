"""
Реализуйте функцию-декоратор, которая проверяет доступ к функции по username
пользователя. Все username пользователей хранятся в глобальной области
видимости в списке USERS. При согласии пользователя на авторизацию ему
предлагается ввести username, который также хранится в глобальной области
видимости. Функция должна использовать два декоратора: один для проверки
авторизации вообще, второй — для проверки доступа.
"""

# для проверки авторизации вообще
def is_auth(func):
    def wrapper():
        if auth:
#            print("Пользователь авторизован")
            func()
        else:
            print("Пользователь не авторизован. Функция выполнена не будет")
    return wrapper

# для проверки доступа
def has_access(func):
    def wrapper():
        if username in USERS:
            print("Пользователь авторизован как", username)
            func()
        else:
            print("Доступ пользователю", username, "запрещён")
    return wrapper


USERS = ['admin', 'guest', 'director', 'root', 'superstar']

yesno = input("""Если хотите авторизоваться, ведите Y, или введите N,
             если хотите продолжить работу как анонимный пользователь: """)

auth = yesno == "Y"

if auth:
    username = input("Введите ваш username: ")

@is_auth
@has_access
def from_db():
    print("some data from database")

from_db()
