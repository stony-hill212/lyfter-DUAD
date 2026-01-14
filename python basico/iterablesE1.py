my_list=[]
list_numbers=int(input("Cantidad de numeros a ingresar: "))
for i in range(list_numbers):
    current_num=int(input(f"Ingrese el numero {i+1}: "))
    my_list.append(current_num)
find_num=int(input("Ingrese un numero para ver la cantidad de veces que se repite: "))
count=my_list.count(find_num)
print(f"El numero {find_num}, se repite {count} veces.")    