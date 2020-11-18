def reverse_str(string):
   if len(string) <= 1:
       return string
   return string[-1] + reverse_str(string[1:-1:]) + string[0]

print(reverse_str('1234567'))

# Вариант записи:
# def reverse_str(string):
#   return \
#          string \
#          if len(string) <= 1 else \
#          string[-1] + reverse_str(string[1:-1:]) + string[0]
