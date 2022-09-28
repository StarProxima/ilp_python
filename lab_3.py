# Задание 3 Дробная часть. Дано положительное действительное число .
# Выведите его дробную часть.

from math import floor


x = float(input())
print(x - floor(x))
