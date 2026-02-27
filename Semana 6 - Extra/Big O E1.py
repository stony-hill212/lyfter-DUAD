#version 1
def manual_add(n):
    result = 0
    for i in range(1, number + 1): #O(n)
        result += i
    return result

#version 2
def add_formula(n):
    return number * (number + 1) // 2  #O(1)


#Respuesta:
#Seria la misma complejidad en ambas versiones, ya que, segun mi entendimiento, 
# Big O seria para clasificar dificultad del algoritmo y no un valor determinado.

#En la version 1 tendria 1 000 000 000 de iteraciones pero el tiempo incrementa directamente con n,
#por lo cual el valor la variable "number" es irrelevante.

# La version 2 resuelve 3 operaciones aritmeticas, 
# pero el tiempo en correr la operacion es el mismo sin importar el valor numerico. 