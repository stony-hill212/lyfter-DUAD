import csv
def get_positiveint(prompt):
    while True:
        try:
            value=int(input(prompt))
            if value<=0:
                raise ValueError
            return value
        except ValueError:
            print("Ingresar un numero positivo.")

def empty_spaces(prompt):
    while True:
        value=input(prompt).strip()
        if value:
            return value
        print("Este espacio no puede quedar vacio.")

def get_validPT(prompt):
    valid={"E","T","M"}
    while True:
        value=input(prompt).upper()
        if value in valid:
            return value
        print("Invalido, usar E, T o M.")

def save_vgames_csv(target):
    n=get_positiveint("Cantidad de juegos por ingresar: ")
    with open(target,mode="w",newline="",encoding="utf-8")as file:
        writer=csv.writer(file)
        writer.writerow(["Nombre", "Genero", "Desarrollador", "PT"])
        for i in range(n):
            print(f"\nJuego {i+1}")
            name=input("Nombre: ")
            gender=input("Genero: ")
            developer=input("Desarrollador: ")
            PT=input("Clasificación ESRB: ")
            writer.writerow([name,gender,developer,PT])
    print("Archivo CSV creado.") 


save_vgames_csv("juegos1.csv")  
import os
print(os.getcwd())        
