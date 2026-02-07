from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    @abstractmethod
    def calculate_perimeter(self):
        pass

import math

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        return math.pi*self.radius**2
    def calculate_perimeter(self):
        return 2*math.pi*self.radius

class Square(Shape):
    def __init__(self,side):
        self.side=side
    def calculate_area(self):
        return self.side**2
    def calculate_perimeter(self):
        return 4*self.side

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def calculate_area(self):
        return self.width*self.height
    def calculate_perimeter(self):
        return 2*(self.width+self.height)

shapes=[
    Circle(5),
    Square(4),
    Rectangle(3,6)
]
for shape in shapes:
    print(type(shape).__name__)
    print("Area:",shape.calculate_area())
    print("Perimeter:", shape.calculate_perimeter())
    print()