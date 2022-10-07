def task1():
    class Cat():
        def __init__(self, name, color, weight):
            self.name = name
            self.color = color
            self.weight = weight

        def meow(self):
            print(f"{self.name}: MEEEOWW")

    cat = Cat("Вася", "amber", 4)
    cat.meow()


def task2():
    class Animal():
        def __init__(self, name):
            self.name = name
            print(f"Родилось животное {name}")

        def eat(self):
            print("Намнём")

        def setName(self, name):
            self.name = name

        def getName(self):
            return self.name

        def MakeNoise(self):
            print(f"{self.name} говорит: Гррр")

    animal = Animal("Гарфилд")
    animal.getName()
    animal.setName("Барсик")
    animal.eat()
    animal.MakeNoise()


def task3():
    class StringVar:
        def __init__(self, str_):
            self.str_ = str(str_)

        def set(self, new_str):
            self.str_ = new_str

        def get(self):
            return self.str_

    some_str = StringVar("abcd")
    print(some_str.get())
    some_str.set("text")
    print(some_str.get())


def task4():
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return f"({self.x}, {self.y})"

        def __add__(self, other):
            return Point(self.x + other.x, self.y + other.y)

        def __sub__(self, other):
            return Point(self.x - other.x, self.y - other.y)

        def __mul__(self, other):
            return Point(self.x * other.x, self.y * other.y)

        def __truediv__(self, other):
            return Point(self.x / other.x, self.y / other.y)

        def __floordiv__(self, other):
            return Point(self.x // other.x, self.y // other.y)

        def __mod__(self, other):
            return Point(self.x % other.x, self.y % other.y)

        def length(self):
            return (self.x ** 2 + self.y ** 2) ** 0.5

        def normolize(self):
            len_ = self.length()
            return Point(self.x / len_, self.y / len_)

    p1 = Point(5, 2)
    p2 = Point(1, 4)
    print(p1 + p2)
    print(p1 - p2)
    print(p1 * p2)
    print(p1 / p2)
    print(p1 // p2)
    print(p1 % p2)
    print(p1.length())
    p2 = p1.normolize()
    print(p2)
    print(p2.length())


def task5():
    class Animal():
        def __init__(self, name):
            self.name = name
            print(f"Родилось животное {name}")

        def eat(self):
            print("Намнём")

        def setName(self, ch_name):
            self.name = ch_name

        def getName(self):
            return self.name

        def MakeNoise(self):
            print(f"{self.name} говорит: Гррр")

    class Cat(Animal):
        def __init__(self, name, color, weight):
            super().__init__(name)
            self.color = color
            self.weight = weight
            print("Родился кот")

        def meow(self):
            print(f"{self.name}: MEEEOWW")

        def MakeNoise(self):
            print(f"{self.name} говорит: Мяу")

    cat = Cat("Эдвард", "Синий", 1)
    cat.meow()
    cat.MakeNoise()


def task6():
    class Animal():
        def __init__(self, name):
            self.name = name
            print(f"Родилось животное {name}")

        def eat(self):
            print("Намнём")

        def setName(self, ch_name):
            self.name = ch_name

        def getName(self):
            return self.name

        def MakeNoise(self):
            print(f"{self.name} говорит: Гррр")

    class Dog(Animal):
        def __init__(self, name, color, weight):
            super().__init__(name)
            self.color = color
            self.weight = weight
            print("Родилась собака")

        def meow(self):
            print(f"{self.name}: ГаАаАаВ")

        def MakeNoise(self):
            print(f"{self.name} говорит: Гав")

    dog = Dog("Собака1", "цвет1", 10)
    dog.meow()
    dog.MakeNoise()


def task7():
    class Animal():
        def __init__(self, name):
            self.name = name
            print(f"Родилось животное {name}")

        def eat(self):
            print("Намнём")

        def setName(self, ch_name):
            self.name = ch_name

        def getName(self):
            return self.name

        def MakeNoise(self):
            print(f"{self.name} говорит: Гррр")

    class Cat(Animal):
        def __init__(self, name, color, weight):
            super().__init__(name)
            self.color = color
            self.weight = weight
            print("Родился кот")

        def meow(self):
            print(f"{self.name}: MEEEOWW")

        def MakeNoise(self):
            print(f"{self.name} говорит: Мяу")

    class Dog(Animal):
        def __init__(self, name, color, weight):
            super().__init__(name)
            self.color = color
            self.weight = weight
            print("Родилась собака")

        def meow(self):
            print(f"{self.name}: ГаАаАаВ")

        def MakeNoise(self):
            print(f"{self.name} говорит: Гав")

    some_cat = Cat("Кот1", "ЦветКота1", 3)
    some_cat.meow()
    some_cat.MakeNoise()
    some_dog = Dog("Собака1", "ЦветСобаки1", 10)
    some_dog.MakeNoise()
    some_dog_2 = Dog("Собака2", "ЦветоСобаки2", 5)
    some_dog_2.MakeNoise()
    some_animal = Animal("Primary creature")
    some_animal.MakeNoise()


def main():
    print('адание 1:')
    task1()
    print('адание 2:')
    task2()
    print('адание 3:')
    task3()
    print('адание 4:')
    task4()
    print('адание 5:')
    task5()
    print('адание 6:')
    task6()
    print('Задание 7:')
    task7()


main()
