# На вход программы подается число. Мы хотим проверить, является ли оно целым, находится ли в
# определенном промежутке (например от 100 до 999 включительно), да еще и делится ли на 2 и 3 одновременно.

a = int(input('Введите число а '))

if a is int(a):
    if 100 <= a <= 999:
        if a % 2 == 0 and a % 3 == 0:
            print('Число отвечает всем условиям')
        else:
            print('Число не подходит - не делится одновременно на 2 и на 3')
    else:
        print('Число не подходит - не из диапазона от 100 до 999')
else:
    print('Число не подходит - не целое')
