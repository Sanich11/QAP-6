"""
Напишите программу, которая получает от пользователя имя файла, открывает
этот файл в текущем каталоге, читает его и выводит два слова: наиболее
часто встречающееся из тех, что имеют размер более трех символов, и наиболее
длинное слово на английском языке.
В файле ожидается смешанный текст на двух языках — русском и английском.
"""


def changeText(text):
    """
    Функция принимает строку с текстом. Убирает все знаки препинания и
    возвращает список, состоящий из слов текста.
    """

    for i in '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~':
        text = text.replace(i, '')

    return text.split()


def mostCommon(text, lenght = 0):
    """
    Функция принимает список и ограничение по длине.
    Возвращает самый часто встречающийся элемент.
    Если есть несколько элементов с одинаковой самой большой частотой,
    то вернёт их все.
    """

    most_common = []
    qty_most_common = 0

    for item in text:
        if len(item) > lenght:
            qty = text.count(item)
            if qty > qty_most_common and qty > 2:
                qty_most_common = qty
                most_common = [item]
            elif qty == qty_most_common:
                most_common.append(item)

    return list(set(most_common))

def mostLenght(text):
    """
    Функция принимает список. Возвращает самый длинный элемент. Если есть
    несколько элементов с одинаковой самой большой длиной, то вернёт их все.
    """

    most_lenght = []
    qty_most_lenght = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for item in text:
        for char in item:
            if char not in alphabet:
                charEn = False
            else:
                charEn = True

        if charEn:
            qty = len(item)
            if qty > qty_most_lenght:
                qty_most_lenght = qty
                most_lenght = [item]
            elif qty == qty_most_lenght:
                most_lenght.append(item)

    return list(set(most_lenght))

nameFile = input('Введите название файла: ')

with open(nameFile, encoding='utf8') as f:
    fileText = f.read()

fileText = changeText(fileText)
print(f'Список самых частых слов более 3х символов: {mostCommon(fileText, 3)}')
print(f'Список самых длинных английскиих слов: {mostLenght(fileText)}')
