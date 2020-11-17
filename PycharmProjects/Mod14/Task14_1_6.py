"""
    Напишите функцию, которая проверяет, является ли данная строка палиндромом
    или нет, и возвращается результат проверки (True, False).
"""

def check_palindrome(text):
    text = text.lower()
    text = text.replace(' ', '')
    if text == text[::-1]:
        return True
    return False

check_palindrome('Кит на море не романтик')
