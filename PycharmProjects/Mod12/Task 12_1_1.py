a = [1, 2, 3, 4]
b = ['1', '2', '3']
a += a
b *= 2
c = a[::-3] + b[1:3]
print(len(c))