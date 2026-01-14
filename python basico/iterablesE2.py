my_list=[]
amount_n=int(input("Cantidad de numeros a ingresar: "))
for i in range(amount_n):
    current_num=int(input(f"Ingrese el numero {i+1}: "))
    my_list.append(current_num)
positive_nums=True
for n in my_list:
    if n<=0:
        positive_nums=False
        break
if positive_nums:
    print("Todos los numeros son positivos.")
else:
    print("Hay al menos un numero negativo o cero.")    
