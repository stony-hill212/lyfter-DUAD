my_list=[]
amount_n=int(input("Cantidad de numeros a ingresar: "))
for i in range(amount_n):
    current_num=int(input(f"Ingrese el numero {i+1}: "))
    my_list.append(current_num)
def calculate_sum(num_list):
    total=0
    for num in num_list:
        total+=num
    return total


def show_sum(num_list):
    result=calculate_sum(num_list)
    print(result)
show_sum(my_list)            