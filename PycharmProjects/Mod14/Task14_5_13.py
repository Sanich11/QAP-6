"""
    Реализуйте функцию-генератор, каждое значение которого —
    приближение числа e с некоторым числом n.
    Для вычисления числа e с определенной точностью можно использовать формулу:
                              e_n = (1 + 1/n)**n
"""

# Решение из курса
def e():
    n = 1

    while True:
        yield (1 + 1/n)**n
        n += 1