class Employee:
    def __init__(self,name,salary):
        self._name=name
        self.salary=salary
    @property
    def name(self):
        return self._name
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,value):
        if value<=0:
            raise ValueError("Salary must be a positive number.")
        self._salary=value
    def promote(self,percentage):
        if percentage<=0:
            raise ValueError("Promotion percentage must be positive.")
        self._salary+=self._salary*(percentage/100)

employee=Employee("Uncle Luther",1000)
print(employee.name)
print(employee.salary)
employee.promote(0.5)
print(employee.salary)