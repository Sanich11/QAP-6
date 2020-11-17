number = int(input())

divisor = 2

while number % divisor != 0:
    divisor += 1

if divisor == number:
    print('Число простое')
else:
    print('Число не простое')
