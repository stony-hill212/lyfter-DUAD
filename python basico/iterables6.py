my_list=[]
amount_n=int(input("Cantidad de numeros a ingresar: "))
for i in range(amount_n):
    current_num=int(input(f"Ingrese el numero {i+1}: "))
    my_list.append(current_num)
even_nums=[]
for n in my_list:
    if n%2==0:
        even_nums.append(n)
print("Numeros pares: ",even_nums)            