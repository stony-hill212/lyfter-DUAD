#version 1
def manual_add(n):
    result = 0
    for i in range(1, number + 1): #O(n)
        result += i
    return result

#version 2
def add_formula(n):
    return number * (number + 1) // 2  #O(1)


#Respuestas: 

#1. #O(n), #O(1)

#2.Si number= 1000 000 000, tendriamos que usar la version 2 ya que a diferencia de la version 1, 
#la version 2 ejecuta varias operacioness aritmicas a la vez y n no aumenta el tiempo, por lo cual, la verion 2
#tendria la misma velocidad si n fuese 10 o 100000000.
