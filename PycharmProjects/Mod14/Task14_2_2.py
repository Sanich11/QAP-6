"""
    Написать функцию, которая будет перемножать любое количество переданных
    ей аргументов.
"""

def multi(*nums):
   mul_ = 1
   for n in nums:
       mul_ *= n

   return mul_


print(multi())  # 1
print(multi(1))  # 1
print(multi(1, 2))  # 2
print(multi(1, 2, 3))  # 6
print(multi(1, 2, 3, 4, 5, 6))  # 720
