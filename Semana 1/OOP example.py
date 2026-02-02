class Fighter:
    def __init__(self,name):
        self.name=name
    
    def intro(self):
        return f"His name is {self.name}"
print(Fighter("GSP").intro())
        