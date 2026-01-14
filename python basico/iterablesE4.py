my_list=[]
amount_n=int(input("Cantidad de numeros a ingresar: "))
for i in range(amount_n):
    current_num=int(input(f"Ingrese el numero {i+1}: "))
    my_list.append(current_num)
average=sum(my_list)/len(my_list)
above_average=[]
for n in my_list:
    if n>average:
        above_average.append(n)
print(f"Promedio: {average}")
print(f"Nueva lista: {above_average}")            