
def linear_solve(a, b):
    if a:
        return b/a
    elif not a and not b: # снова используем числа в логических выражениях
        return "Бесконечное количество корней"
    else:
        return "Нет корней"

print(linear_solve(0,1))
