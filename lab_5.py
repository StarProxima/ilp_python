# Задание 8 Сумма факториалов. По данному натуральном вычислите
# сумму 1! + 2! + 3!+. . . + !. В решении этой задачи можно использовать
# только один цикл. Пользоваться математической библиотекой math в этой
# задаче запрещено.

n = int(input())
sum = 0
fac = 1
for i in range(1, n + 1):
    fac *= i
    sum += fac

print(sum)
