message=input("Ingrese un mensaje/frase/palabra: ")
chars=[]
for i in range(len(message)-1,-1,-1):
    chars.append(message[i])
print(chars)    