class Vehicle:
    def __init__(self,brand,year):
        self._brand=brand
        self._year=year
    def get_info(self):
        return f"{self._year} {self._brand}"

class Car(Vehicle):
    def __init__(self,brand,year,doors):
        super().__init__(brand,year)
        self._doors=doors
    def get_info(self):
        base_info=super().get_info()
        return f"{base_info} - {self._doors} doors"

class Motorcycle(Vehicle):
    def __init__(self,brand,year,bike_type):
        super().__init__(brand,year)
        self._type=bike_type
    def get_info(self):
        base_info=super().get_info()
        return f"{base_info} - type: {self._type}"

vehicle1=Car("Maserati", 2022, 2)
vehicle2=Motorcycle("Triumph", 2021, "Sport")
print(vehicle1.get_info())
print(vehicle2.get_info())