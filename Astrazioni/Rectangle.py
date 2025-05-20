from Shape import Shape

class Rectangle(Shape):
    def __init__(self, base:float, altezza:float):
        self.base = base
        self.altezza = altezza

    def area(self) -> float:
        return self. base * self. altezza
    def perimeter(self):
        return (self. base + self. altezza)*2
    def base(self) -> float:
        return self.__base
    