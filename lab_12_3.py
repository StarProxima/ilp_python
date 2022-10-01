# Задание 13 Что за химический элемент. Напишите программу, которая
# будет считывать файл, содержащий информацию о химических элементах, и
# сохранять ее в более подходящей для этого структуре данных. После этого
# пользователь должен ввести значение. Если введенное значение окажется
# целочисленным, программа должна вывести на экран обозначение и название
# химического элемента с введенным количеством протонов. При вводе
# пользователем строки необходимо отобразить количество протонов элемента
# с введенным пользователем обозначением или названием. Если введенное
# пользователем значение не соответствует ни одному из элементов в файле,
# необходимо вывести соответствующее сообщение об ошибке. Позвольте
# пользователю вводить значения до тех пор, пока он не оставит ввод пустым.


elements = {}

with open('lab_12_3_data.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            number, symbol, name, = line.split(',')
            elements[name] = (symbol, number)
            elements[symbol] = (name, number)
            elements[number] = (symbol, name)

while True:
    value = input('Enter a number or symbol or name: ')
    if not value:
        break
    try:
        value = int(value)
        try:
            (symbol, name) = elements[str(value)]
            print(f'{symbol} {name} {value}')
        except KeyError:
            print(f'No element with {value} protons')
    except ValueError:
        try:
            (name, number) = elements[value]
            print(f'{number} {value}')
        except KeyError:
            print(f'No element with symbol or name {value}')
