from functools import wraps
def fight_logger(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"\nFunction name: {func.__name__}")
        print(f"Positional arguments: {args}")
        print(f"keyword arguments: {kwargs}")
        result=func(*args,**kwargs)
        print(f"Returned value: {result}")
        return result
    return wrapper

@fight_logger
def announce_fight(fighter1,fighter2,weight_class="Middleweight"):
    return f"{fighter1} vs {fighter2} at {weight_class}"

announce_fight("Adesanya","Whittaker")