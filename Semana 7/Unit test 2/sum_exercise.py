def calculate_sum(num_list):
    total=0
    for num in num_list:
        total+=num
    return total


def show_sum(num_list):
    result=calculate_sum(num_list)
    print(result)

if __name__=="main":
    my_list=[]
    amount_n=int(input("Amount of numbers to enter: "))
    for i in range(amount_n):
        current_num=int(input(f"Enter number {i+1}: "))
        my_list.append(current_num)
        
    show_sum(my_list)

