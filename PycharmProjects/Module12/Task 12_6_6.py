# Определяем, являются ли введённые emails валидными

# Пользователь вводит для валидации список email через запятую с пробелом. Отделяем emails по разделителю ', '
# emails пример: qwerty@@qwer.rr, qwerty@qw.er, qwerty.we, q@werwe.ee, qwerty@w.rt, qwewqet, qwerty@we.e, qwerty@w.e.ry

emails = input('Введите, пожалуйста, email адреса через запятую и пробел: ').split(', ')

# Задаём переменную для вывода итогового словаря
emails_dict = {}

# Запускаем проверку email адресов по всему собранному списку
for i in emails:
    if (i.count('@') > 1 or i.count('@') == 0                      # Проверяем, чтобы '@' была и не больше одной
        or len(i.split('@')[0]) < 2 or len(i.split('@')[1]) < 2):  # Проверяем, что есть min 2 знака слева/справа от '@'
        emails_dict[i] = False                                     # Не прошло, складываем этот email в словарь с False
    else:
        domain = i.split('@', 1)[1]                                # Выделяем доменную часть email
        if (domain.count('.') < 1 or len(domain) < 5               # Проверяем, что есть одна '.', а символов не < 5
            or len(domain.split('.')[0]) < 2 or len(domain.split('.')[1]) < 2): # Проверяем, что есть min 2 знака
            emails_dict[i] = False                                 # слева/справа от '.' - нет, опять в словарь с False
        else:
            emails_dict[i] = True                                  # Когда всё в порядке - в словарь с True

for key, values in emails_dict.items():                            # Выводим на печать в столбик
    print(key, values)
