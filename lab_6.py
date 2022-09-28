# Задание 1 Список квадратов. По данному целому числу распечатайте
# все квадраты натуральных чисел, не превосходящие , в порядке возрастания.


def squares(n):
    result = []
    i = 1
    while i ** 2 <= n:
        result.append(i ** 2)
        i += 1
    return result


n = int(input())
print(*squares(n))
