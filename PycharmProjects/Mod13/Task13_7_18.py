# Реализуйте программу, которая сжимает последовательность символов.
# На вход подается последовательность вида: aaabbccccdaa
# Необходимо вывести строку, состоящую из символов и количества повторений
# этого символа. Вывод должен выглядеть как: a3b2c4d1a2

count = 1
letter = []
string = str(input('Введите строку: \n'))

for i in string:
	if string[i] == string[i + 1]:
		count += 1
		letter = i
print(zip(letter, count))
# for i in string:
# 	Letters = Letters.append(i)
#     if string[i] == string[i + 1]:
#     	Count += 1
