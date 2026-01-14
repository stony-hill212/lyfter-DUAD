def user_name():
    while True:
        try:
            name=input("Ingrese su nombre: ")
            if any(char.isdigit()for char in name):
                raise ValueError("El nombre no puede ser numero.")
            return name
        except ValueError as e:
            print(e)

def user_age():
    while True:
        try:
            age=input("Ingrese su edad: ")
            if not age.isdigit():
                raise ValueError("Numero no valido.")
            return int(age)
        except ValueError as e:
            print(e)

name=user_name()
age=user_age()
print(f"Hola {name}, su edad es {age}.")            