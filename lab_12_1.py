# Задание 1 Отображаем начало файла. В операционных системах на базе
# Unix обычно присутствует утилита с названием head. Она выводит первые
# десять строк содержимого файла, имя которого передается в качестве
# аргумента командной строки. Напишите программу на Python, имитирующую
# поведение этой утилиты. Если файла, указанного пользователем, не
# существует, или не задан аргумент командной строки, необходимо вывести
# соответствующее сообщение об ошибке.

import sys

if len(sys.argv) < 2:
    print('Usage: lab_12_1.py filename')
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename) as f:
        for i in range(10):
            line = f.readline()
            if line:
                print(line, end='')
            else:
                break
except FileNotFoundError:
    print('File not found:', filename)
