import random
secret_num=random.randint(1,10)
while True:
    users_guess=int(input("Ingrese un numero del 1 al 10: "))
    if users_guess==secret_num:
        print("Opcion correcta.")
        break
    else:
        print("Opcion incorrecta, intentar nuevamente.")    