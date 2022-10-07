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
