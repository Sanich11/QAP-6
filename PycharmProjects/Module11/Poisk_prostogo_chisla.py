number = int(input())    # Задача 11.6.3 - поиск простого числа
                         # Ещё улучшаем алгоритм - перебор всех нечётных вариантов,
if number % 2 == 0:      # с условием, что число меньше квадрата делителя
    divisor = 2
else:
    divisor = 3

    while divisor ** 2 <= number and number % divisor != 0:
        divisor += 2

if divisor **2 > number:
    print('Число простое')
else:
    print('Число не простое')
