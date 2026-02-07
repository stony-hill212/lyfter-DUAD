class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    
    def total_value(self):
        return self.price*self.quantity

class Inventory:
    def __init__(self):
        self.products=[]

    def add_products(self,product):
        self.products.append(product)
    
    def show_products(self):
        if not self.products:
            print("Inventory is empty.")
            return
        for product in self.products:
            print(
                f"{product.name} | "
                f"Price: {product.price} | "
                f"Quantity: {product.quantity}"
            )
    
    def calculate_total_value_of_inventory(self):
        total=0
        for product in self.products:
            total+=product.total_value()
        return total

def get_positive_float(target):
    while True:
        try:
            value=float(input(target))
            if value<=0:
                raise ValueError("Value must be greater than 0")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")

def get_positive_int(target):
    while True:
        try:
            value=int(input(target))
            if value<0:
                raise ValueError("Value cannot be negative.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")

inventory=Inventory()
while True:
    name=input("Enter product name or 'x' to quit: ")
    if name.lower()=="x":
        break
    price=get_positive_float("Enter product price: ")
    quantity=get_positive_int("Enter product quantity: ")
    product=Product(name,price,quantity)
    inventory.add_products(product)
print("\nProducts in inventory:")
inventory.show_products()
total=inventory.calculate_total_value_of_inventory()
print(f"\nTotal inventory amount: {total:.2f}")

