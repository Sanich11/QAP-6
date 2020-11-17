i = 0              # Конструкция else после цикла while
while True:
    i += 1
    print(i)
    if i == 3:
        break
else:              # Код, написанный в else после цикла не выполнится, если цикл завершается с помощью break.
    print('End')
