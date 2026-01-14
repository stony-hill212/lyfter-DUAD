my_list=[]
amount_n=int(input("Cantidad de numeros a ingresar: "))
for i in range(amount_n):
    current_num=int(input(f"Ingrese el numero {i+1}: "))
    my_list.append(current_num)
find_lowest=my_list[0]
for n in my_list:
    if n<find_lowest:
        find_lowest=n
print(f"El menor valor es: {find_lowest}")            