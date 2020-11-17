"""
Создайте текстовый файл filename.txt с вашей любимой песней
(вручную, через проводник) и попробуйте вывести содержимое
целиком и построчно с помощью методов, рассмотренных выше.
"""


with open(r'c:\Users\Куличенко\Documents\QAPython\Python\sing.txt', 'rt',
          encoding='utf8') as f:
#    print(f.read())
#    print(f.readline())
    print(f.readlines(50))
