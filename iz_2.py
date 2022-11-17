class Money:

    def __init__(self, rubles, kopecks):
        # if (rubles < 0 or kopecks < 0):
        #     raise ValueError("Negative value")

        self.rubles = rubles
        self.kopecks = kopecks
        self = self.normalize()

    def normalize(self):
        if (self.kopecks >= 100):
            self.rubles += self.kopecks // 100
            self.kopecks %= 100
        return self

    def __str__(self):
        return str(self.rubles) + "," + "{:0>2}".format(self.kopecks)

    def __add__(self, other):
        return Money(self.rubles + other.rubles, self.kopecks + other.kopecks).normalize()

    def __sub__(self, other):
        return Money(self.rubles - other.rubles, self.kopecks - other.kopecks).normalize()

    # multiply two money objects and money with int
    def __mul__(self, other):
        if (isinstance(other, int)):
            return Money(self.rubles * other, self.kopecks * other).normalize()
        elif (isinstance(other, Money)):
            num1 = self.rubles * 100 + self.kopecks
            num2 = other.rubles * 100 + other.kopecks
            num = num1 * num2 // 100
            return Money(0, num).normalize()

    # divide two money objects and money with float
    def __truediv__(self, other):
        if (isinstance(other, float) or isinstance(other, int)):
            num1 = self.rubles + (self.kopecks / 100)
            num = num1 / other
            return Money(int(num), int(((num % 1) * 100))).normalize()
        elif (isinstance(other, Money)):
            num1 = self.rubles + (self.kopecks / 100)
            num2 = other.rubles + (other.kopecks / 100)
            num = num1 / num2
            return Money(int(num), int(((num % 1) * 100))).normalize()

    def __eq__(self, other):
        return self.rubles == other.rubles and self.kopecks == other.kopecks

    def __lt__(self, other):
        if (isinstance(other, Money)):
            return self.rubles < other.rubles or (self.rubles == other.rubles and self.kopecks < other.kopecks)
        elif (isinstance(other, float) or isinstance(other, int)):
            return self.rubles < int(other) or (self.rubles == int(other) and self.kopecks < (other % 1) * 100)

    def __gt__(self, other):
        if (isinstance(other, Money)):
            return self.rubles > other.rubles or (self.rubles == other.rubles and self.kopecks > other.kopecks)
        elif (isinstance(other, float) or isinstance(other, int)):
            return self.rubles > int(other) or (self.rubles == int(other) and self.kopecks > (other % 1) * 100)

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other


if __name__ == '__main__':
    a = Money(1, 95)
    b = Money(3, 107)

    print(a)
    print(b)

    print("Сложение", a + b)
    print("Вычитание", a - b)
    print("Умножение на число", a * 2)
    print("Умножение", a * b)
    print("Деление на число", a / 2)
    print("Деление", a / b)
    print("Равенство", a == b)
    print("Меньше числа", a < 2)
    print("Меньше", a < b)
    print("Больше числа", a > 2)
    print("Больше", a > b)

    print("less than", a < 1.5)
    print("less than", a < 1.95)
    print("less than", a < 1.96)

    print("greater than", a > 1.5)
    print("greater than", a > 1.95)
    print("greater than", a > 1.96)

    print("less than", a < Money(1, 50))
    print("less than", a <= Money(1, 95))
    print("less than", a < Money(1, 96))
