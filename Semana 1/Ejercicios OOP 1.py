import math

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def get_area(self):
        return math.pi*(self.radius**2)
    
    def get_circumference(self):
        return 2*math.pi*self.radius

c=Circle(6)
print(c.get_area())
print(c.get_circumference())