# Задание 5 Парты. В школе решили набрать три новых математических
# класса. Так как занятия по математике у них проходят в одно и то же время,
# было решено выделить кабинет для каждого класса и купить в них новые
# парты. За каждой партой может сидеть не больше двух учеников. Известно
# количество учащихся в каждом из трёх классов. Сколько всего нужно закупить
# парт чтобы их хватило на всех учеников? Программа получает на вход три
# натуральных числа: количество учащихся в каждом из трех классов.

class1 = int(input())
class2 = int(input())
class3 = int(input())

print(class1 // 2 + class1 % 2 + class2 // 2 + class2 %
      2 + class3 // 2 + class3 % 2)
