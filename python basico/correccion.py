def scope_experiment():
    x=10
    return x
value=scope_experiment()
print(value)
counter=0

def increment():
    global counter
    counter+=1
print(counter)
increment()
increment()
print(counter)    