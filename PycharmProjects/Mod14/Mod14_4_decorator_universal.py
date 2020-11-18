# Вот универсальный шаблон для декоратора:

def my_decorator(fn):
    print("Этот код будет выведен один раз в момент декорирования функции")
    def wrapper(*args, **kwargs):
        print('Этот код будет выполняться перед каждым вызовом функции')
        result = fn(*args, **kwargs)
        print('Этот код будет выполняться после каждого вызова функции')
        return result
    return wrapper
    