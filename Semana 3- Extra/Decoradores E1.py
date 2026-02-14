from functools import wraps

def repeat_twice(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        func(*args,**kwargs)
    return wrapper

@repeat_twice
def message(name):
    print(f"Hola, {name}")

def main():
    message("Jeanca")

if __name__=="__main__":
    main()
