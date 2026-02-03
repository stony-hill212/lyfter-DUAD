class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    
    def get_area(self):
        return self.width*self.height
    
    def get_perimeter(self):
        return 2*(self.height+self.width)

def get_positive(target):
    while True:
        try:
            number=float(input(target))
            if number<=0:
                raise ValueError("Value must be greater than 0")
            return number
        except ValueError as e:
            print(f"Ivalid input: {e}")

height=get_positive("Please enter the height: ")
width=get_positive("Please enter the width: ")
rectangle=Rectangle(width,height)
print(rectangle.get_area())
print(rectangle.get_perimeter())
