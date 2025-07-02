from Shape import Shape

import math

class Circle(Shape):
    def __init__(self, r:float):
        super().__init__()
        self. __r: float = r
    
    def area(self)-> float:
        return math.pow(self. __r, 2)*math.pi
    
    def perimeter(self):
        return 2 * math.pi * self.__r
    

if __name__ == "__main__":
    c = Circle(10.3)
    print(c.area())
    print(c.perimeter())