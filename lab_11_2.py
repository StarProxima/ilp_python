# Задание 10 Продажи. Дана база данных о продажах некоторого
# интернет-магазина. Каждая строка входного файла представляет собой запись
# вида Покупатель товар количество, где Покупатель – имя покупателя(строка без пробелов), товар – название товара(строка без пробелов),
# количество – количество приобретенных единиц товара.
# Создайте список всех покупателей, а для каждого покупателя подсчитайте количество приобретенных им единиц каждого вида товаров.
# Список покупателей, а также список товаров для каждого покупателя нужно
# выводить в лексикографическом порядке.
# Входные данные
# Ivanov paper 10
# Petrov pens 5
# Ivanov marker 3
# Ivanov paper 7
# Petrov envelope 20
# Ivanov envelope 5
# Правильный ответ
# Ivanov:
# envelope 5
# marker 3
# paper 17
# Petrov:
# envelope 20
# pens 5

import sys


if len(sys.argv) != 2:
    print('Usage: python3 lab_11_2.py <file>')
    sys.exit(1)

with open(sys.argv[1], 'r') as f:
    data = f.read().splitlines()

customers = {}
for line in data:
    customer, item, count = line.split()
    if customer not in customers:
        customers[customer] = {}
    if item not in customers[customer]:
        customers[customer][item] = 0
    customers[customer][item] += int(count)

for customer in sorted(customers):
    print(customer + ':')
    for item in sorted(customers[customer]):
        print(item, customers[customer][item])
