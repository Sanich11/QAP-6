"""
    Дано натуральное восьмизначное число. Выясните, является ли оно палиндромом (читается одинаково
    слева направо и справа налево).

    (Подсказка: использовать целочисленное деление и деление с остатком не нужно. Попробуйте преобразовать
    число к строке, а потом перевернуть эту строку).
"""

num = 12344321

print(str(num) == str(num)[::-1])
