string = input().replace(' ', '').lower()     # пользователь вводит строку, мы убираем пробелы и переводим в строчные

for i in range(len(string) // 2):
    if string[i] != string[-1-i]:
        print('Это не палиндром')
        break
else:
    print('Это палиндром')