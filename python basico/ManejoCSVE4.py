import csv
import os
def get_no_empty(prompt):
    while True:
        value=input(prompt).strip()
        if value:
            return value
        print("El espacio no puede quedar vacio.")

def print_games():
    base_dir=os.path.dirname(os.path.abspath(__file__))
    file_path=os.path.join(base_dir,"juegos1.csv")
    user_input=get_no_empty("Ingerese un desarrollador: ").lower()
    found=False
    try:
        with open(file_path,"r",encoding="utf-8")as file:
            reader=csv.reader(file)
            next(reader)
            for row in reader:
                if row[2].lower()==user_input:
                    print(", ".join(row))
                    found=True
        if not found:
            print("Ningun juego con ese desarrollador.")
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print("Error:", e)

print_games()
