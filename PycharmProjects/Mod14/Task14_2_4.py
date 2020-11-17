"""
    С помощью рекурсивной функции развернуть строку.
"""

def rev_str(text):
    if len(text) == 0:
        return ''
    return text[-1] + rev_str(text[:-1])

print(rev_str('123456789'))
print(rev_str('987654321'))
