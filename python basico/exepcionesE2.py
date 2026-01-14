def convertir_a_entero(values):
    result=[]
    print("Resultado:")
    for value in values:
        try:
            converted=int(value)
            print(f'"{value}",convertido a {converted}.')
            result.append(converted)
        except(ValueError,TypeError):
            print(f"No se pudo convertir el elemento: {value}")
    return result        

my_list=[]
while True:
    try:
        amount_values=int(input("Catidad de valores por ingresar: "))
        for i in range(amount_values):
            current_value=input(f"Ingrese el valor numero {i+1}: ")
            my_list.append(current_value)
        break    
    except(ValueError,TypeError):
        print("caracter invalido.")
                

numbers=convertir_a_entero(my_list)    
print("Numeros validos:",numbers)

