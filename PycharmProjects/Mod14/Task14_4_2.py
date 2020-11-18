"""
Напишите декоратор, который будет подсчитывать количество вызовов декорируемой функции. 
Для хранения переменной содержащей, количество вызовов, используйте nonlocal область декоратора.
"""


def count_decorator(fn):
    x = 0

    def wrapper(*args, **kwargs):
        nonlocal x
        x += 1
        fn(*args, **kwargs)
        print(f"Функция {fn} была вызвана {x} раз")

    return wrapper


@count_decorator
def my_func():
	print('My function with decorator')


my_func()
my_func()
my_func()
