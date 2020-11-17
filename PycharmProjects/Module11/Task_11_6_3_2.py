number = int(input())

if number % 2 == 0:
    divisor = 2
else:
    divisor = 3

while number % divisor != 0:
    divisor += 2

if divisor == number:
    print('Число простое')
else:
    print('Число не простое')
