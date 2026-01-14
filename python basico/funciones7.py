
def filt_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


def show_primes(numbers):
    primes=[]
    for num in numbers:
        if filt_prime(num):
            primes.append(num)
    return primes

my_list=[]
amount_n=int(input("Amount of numbers: "))
for i in range(amount_n):
    current_num=int(input(f"Please enter value # {i+1}: "))
    my_list.append(current_num)
print(show_primes(my_list))