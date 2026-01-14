list_numbers=[]
for _ in range(10):
    req_numbers=int(input("Ingrese un numero: "))
    list_numbers.append(req_numbers)
highest_num=max(list_numbers)
print(list_numbers,"El numero mas alto es: ",highest_num)    
