from functools import wraps
from datetime import datetime

def Validate_numbers(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        all_values=list(args)+list(kwargs.values())
        for value in all_values:
            if not isinstance(value,(int,float)):
                raise TypeError(f"Invalid argument: {value}")
        return func(*args,**kwargs)
    return wrapper

def log_call(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        current_time=datetime.now()
        print(f"\nFunction: {func.__name__}")
        print(f"Arguments: {args}")
        print(f"Keyword arguments: {kwargs}")
        print(f"Date: {current_time}")
        result=func(*args,**kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@log_call
@Validate_numbers
def multiply(a,b):
    return a*b

def main():
    print("---Valid call---")
    multiply(3,4)
    print("\n---Invalid call---")
    try:
        multiply(3,"four")
    except TypeError as e:
        print("Error:", e)

if __name__=="__main__":
    main()