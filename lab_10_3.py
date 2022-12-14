# Задание 7 Угадай число. Август и Беатриса играют в игру. Август
# загадал натуральное число от 1 до n. Беатриса пытается угадать это число, для
# этого она называет некоторые множества натуральных чисел. Август отвечает
# Беатрисе YES, если среди названных ей чисел есть задуманное или NO в
# противном случае. После нескольких заданных вопросов Беатриса запуталась
# в том, какие вопросы она задавала и какие ответы получила и просит вас
# помочь ей определить, какие числа мог задумать Август.
# В первой строке задано – максимальное число, которое мог загадать
# Август. Далее каждая строка содержит вопрос Беатрисы (множество чисел,
# разделенных пробелом) и ответ Августа на этот вопрос.
# Вы должны вывести через пробел, в порядке возрастания, все числа,
# которые мог задумать Август.
# Входные данные
# 10
# 1 2 3 4 5
# YES
# 2 4 6 8 10
# NO
# HELP
# Правильный ответ
# 1 3 5


n = int(input())
s = set(range(1, n + 1))

while True:
    question = input().split()
    if question[0] == 'HELP':
        print(*s)
        break
    if input() == 'YES':
        s &= set(map(int, question))
    else:
        s -= set(map(int, question))
