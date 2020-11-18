# Написать цикл с использованием whilе,
# который возводит числа в квадрат, пока результат меньше 1000.

S = 0  # заводим переменную счетчик, в которой мы будем считать произведение
n = 1  # текущее натуральное число

# заводим цикл while, который будет работать пока произведение не превысит 1000
while S < 1000:  # делай пока ...
    S = n ** 2  # возводим числа в квадрат
    n += 1  # так как сумма ещё не достигла нужного значения, то увеличиваем переменную счетчик
    print("Ещё считаю ...")

print("Произведение равно: ", S)
print("Количество чисел: ", n)
