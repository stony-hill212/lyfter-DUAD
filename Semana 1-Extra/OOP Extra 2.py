class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        return"makes a sound"

class Dog(Animal):
    def speak(self):
        return"bark"


class Cat(Animal):
    def speak(self):
        return"meow"

dog=Dog("Santa's helper")
cat=Cat("Whiskers")
print(dog.speak()) 
print(cat.speak()) 
