# Задание 4 Встречалось ли число раньше. Во входной строке записана
# последовательность чисел через пробел. Для каждого числа выведите слово
# YES (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.
# Входные данные
# 1 2 3 2 3 4
# Правильный ответ
# NO
# NO
# NO
# YES
# YES
# NO

set = set()

for x in input().split():
    if x in set:
        print('YES')
    else:
        print('NO')
        set.add(x)
