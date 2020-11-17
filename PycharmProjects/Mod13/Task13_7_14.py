"""
    Модифицируйте пример B = [int(input()) for i in range(5)] так, чтобы в список сохранялось True,
    если элемент четный, и False, если элемент нечетный.
"""

C = [int(input()) % 2 == 0 for i in range(5)]

print(C)
