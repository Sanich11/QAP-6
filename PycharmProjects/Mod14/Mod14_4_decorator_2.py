# декоратор, в котором встроенная функция умеет принимать аргументы
def do_it_twice(func):
   def wrapper(*args, **kwargs):
       func(*args, **kwargs)
       func(*args, **kwargs)
   return wrapper

@do_it_twice
def say_word(word):
   print(word)

say_word("Oo!!!")
# Oo!!!
# Oo!!!
