class Rectangle:
    def __init__(self,width,height):
        self.width=self.get_positive(width,"width")
        self.height=self.get_positive(height,"height")
    
    def get_positive(self,value,name):
        if value<0:
            raise ValueError(f"Error: {name}, value must be a positive number.")
        return value
    
    def get_area(self):
        return self.height*self.width
    
    def get_perimeter(self):
        return 2*(self.height+self.width)
try:
    w=float(input("Please enter the width: "))
    h=float(input("Please enter the height: "))
    rectangle=Rectangle(w,h)
except ValueError as e:
    print(f"Invalid input:{e}")

print(rectangle.get_area())
print(rectangle.get_perimeter())

