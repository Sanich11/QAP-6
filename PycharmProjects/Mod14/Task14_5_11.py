"""
реализовать функцию equal(N, S), проверяющую, совпадает ли сумма цифр числа N
с числом S. При написании программы следует обратить внимание на то, что,
если S стала отрицательной, то необходимо сразу вернуть False.
"""

# def sum_num(N):
#     if N < 10:
#         return N
#     return N % 10 + sum_num(N // 10)
#
# def equal(N, S):
#     if S < 0:
#         return False
#     return True if sum_num(N) == S else False
#
# print(equal(252, 9))

# Решение с курса
def equal(N, S):
    if S < 0:
        return False
    if N < 10:
        return N == S
    else:
        return equal(N // 10, S - N % 10)
