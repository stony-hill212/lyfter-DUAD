from functools import wraps

def numbers_only(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        all_values=list(args)+list(kwargs.values())
        for value in all_values:
            if not isinstance(value,(int,float)):
                raise TypeError(f"Invalid character: '{value}', only number are allowed.")
        return func(*args,**kwargs)
    return wrapper

@numbers_only
def calculate_total_strikes(jabs,crosses,kicks=0):
    return jabs+crosses+kicks

def main():
    print("---Valid call---")
    total=calculate_total_strikes(30,20,kicks=10)
    print("Total strikes:", total)
    print("\n---Invalid call---")
    try:
        calculate_total_strikes(30,"twenty",kicks=10)
    except TypeError as error:
        print("Error:", error)

if __name__=="__main__":
    main()