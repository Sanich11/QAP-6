"""
    Модифицируйте функцию quadratic_solve(a,b,c), чтобы она возвращала
    единственный корень при условии нулевого дискриминанта.
"""


def D(a, b, c):
    return b**2 - 4*a*c

def quadratic_solve(a,b,c):
    if D(a, b, c) < 0:
        return 'Нет вещественных корней'
    elif D(a, b, c) == 0:
        return -b/(2*a)
    else:
        return (-b-D(a,b,c)**0.5)/(2*a), (-b+D(a,b,c)**0.5)/(2*a)

# разбили строку из input и преобразовали к float
L = list(map(float, input('Введите переменные a, b, c').split()))
# передаём список в аргументы функции, используя операцию распаковки
print(quadratic_solve(*L))
