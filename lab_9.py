# Задание 6 Поменять столбцы. Дан двумерный массив и два числа: и .
# Поменяйте в массиве столбцы с номерами и и выведите результат.
# Программа получает на вход размеры массива и , затем элементы
# массива, затем числа и .
# Решение оформите в виде функции swap_columns(a, i, j).

def swap_columns(a, i: int, j: int):
    for row in a:
        row[i], row[j] = row[j], row[i]
    return a


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
i, j = map(int, input().split())

a2 = swap_columns(a, i, j)

for row in a:
    print(*row)
