class NumberOperations:
    def sum_numbers(self,numbers):
        return sum(numbers)
    
    def average(self,numbers):
        if len(numbers)==0:
            return 0
        return sum(numbers)/len(numbers)
    
    def celsius_to_fahrenheit(self,celsius):
        return(celsius*9/5)+32
    
