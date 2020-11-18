# Напишите функцию, которая печатает “обратную лесенку” следующего типа:

# n = 3     n = 4
# ***       ****
# **        ***
# *         **
#           *

def ladder_print(n):
	print(f'n = {n}')
	for i in range(n, 0, -1):
		print('*' * i)

ladder_print(4)
ladder_print(9)
