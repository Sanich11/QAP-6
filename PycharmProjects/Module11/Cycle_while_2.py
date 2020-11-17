a = 1       # Бесконечный цикл и управляющие конструкции break и continue
b = 0
while True:
    if b == 0:
        print('b = 0')
    else:
        print(a)
        a += 1
    b += 1
    if b == 3:
        continue           # continue — команда для пропуска шага (итерации) цикла
    if b == 4:
        break              # break — команда нужна для досрочного выхода из цикла
    print('----')
print('Конец')
