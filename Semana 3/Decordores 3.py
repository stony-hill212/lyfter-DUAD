from datetime import date
from functools import wraps

class User:
    def __init__(self,date_of_birth):
        self.date_of_birth=date_of_birth
    
    @property
    def age(self):
        today=date.today()
        years=today.year-self.date_of_birth.year
        if(today.month,today.day)<(self.date_of_birth.month,self.date_of_birth.day):
            years-=1
        return years

def over_18_required(func):
    @wraps(func)
    def wrapper(user,*args,**kwargs):
        if not isinstance(user,User):
            raise TypeError("First argument must be a User instance.")
        if user.age<18:
            raise PermissionError(f"Access denied, user is {user.age} years old.")
        return func(user,*args,**kwargs)
    return wrapper

@over_18_required
def enter_fight_event(user):
    return f"Access granted, user is {user.age} years old."

def main():
    adult=User(date(1995,6,10))
    minor=User(date(2012,4,3))
    print("---Adult attempt---")
    print(enter_fight_event(adult))
    print("\n---Minor attempt---")
    try:
        print(enter_fight_event(minor))
    except PermissionError as e:
        print("Error:", e)

if __name__=="__main__":
    main()