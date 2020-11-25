# алгоритм для сортировки по убыванию

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

for i in range(len(array)):
    idx_max = i
    for j in range(i, len(array)):
        if array[j] > array[idx_max]:
            idx_max = j
    if i != idx_max:
        array[i], array[idx_max] = array[idx_max], array[i]

print(array)
