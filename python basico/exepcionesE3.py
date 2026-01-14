def sumar_valores(items):
    total=0.0
    for value in items:
        try:
            converted=float(value)
            total+=converted
            print(f"{converted} sumado correctamente.")
        except(ValueError,TypeError):
            print(f"Elemeto invalido: {value}")
    print("Total de la suma:",total) 

my_list=[]
while True:
    try:
        amount_values=int(input("Catidad de valores por ingresar: "))
        for i in range(amount_values):
            current_value=input(f"Ingrese el valor numero {i+1}: ")
            my_list.append(current_value)
        break
    except(ValueError,TypeError):
        print("Ingrese un valor numerico.")    


sumar_valores(my_list)