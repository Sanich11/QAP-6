# В общем виде конструкция генератора списков записывается следующим образом:

L = [a for a in some_iter_obj if cond]

# Напишем генератор списков, в котором будут храниться квадраты первых 10 натуральных чисел.

squares = [i**2 for i in range(1,11)]

# Модифицируем этот генератор списков так, что в список будут включаться квадраты только от нечетных чисел.

squares_num = [i**2 for i in range(1,11) if i % 2 == 1]

# Тип элемента, который будет включаться в список может быть любым. Например, можно составить список из кортежей:

list_tuples = [(i, i**2) for i in range(1,11)]

# А используя вложенные генераторы списков можно создать матрицу «одним махом»:

M = [[i+j for j in range(5)] for i in range(5)]
# В данном случае мы на каждой итерации цикла с индексом i создавали вложенный список с индексами j,
# что в итоге позволило создать матрицу (таблицу чисел).

# Интересный эффект образуется в сочетании использования генераторов списков и функции input().
# На каждой итерации цикла консоль будет запрашивать данные для ввода и сохранять их в качестве элемента списка.

B = [input() for i in range(5)]

# Приведенный выше пример 5 раз запросит у пользователя данные для входа и запишет их в список.
# Здесь же можно использовать сразу преобразование в необходимый тип, если он заранее известен.

C = [int(input()) for i in range(5)]
