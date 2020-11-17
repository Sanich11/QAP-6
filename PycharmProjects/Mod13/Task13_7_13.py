""" При помощи генератора списков создайте таблицу умножения чисел от 1 до 10. """

multi_table = [[i * j for i in range(1, 11) for j in range(1, 11)]]

print(multi_table)
# for m in multi_table: print(*m)
