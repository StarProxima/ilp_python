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
