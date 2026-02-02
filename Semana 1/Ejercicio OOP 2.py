class Bus:
    def __init__(self,max_passengers):
        self.max_passengers=max_passengers
        self.passengers=0
    
    def add_passenger(self):
        if self.passengers<self.max_passengers:
            self.passengers+=1
            print("Passenger added.")
        else:
            print("Bus is at maximum capacity.")
    
    def remove_passenger(self):
        if self.passengers>0:
            self.passengers-=1
            print("Passenger removed.")
        else:
            print("Bus is empty.")

b=Bus(6)
b.add_passenger()  #EX
b.add_passenger()  #EX
b.add_passenger()  #EX
b.add_passenger()   #EX
b.remove_passenger() #EX
print(b.__dict__)