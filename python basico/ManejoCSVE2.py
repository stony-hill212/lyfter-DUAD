import csv
import os
def get_valid_rating():
    valid={"E","T","M"}
    while True:
        PT=input("Ingrese la clasificacion parental (E, T o M): ").strip().upper()
        if PT in valid:
            return PT
        print("Clasificacion invalida, usar E, T o M.")

def print_pt_csv():
    base_dir=os.path.dirname(os.path.abspath(__file__))
    file_path=os.path.join(base_dir,"juegos1.csv")
    user_input=get_valid_rating()
    found=False
    try:
        with open(file_path,"r",encoding="utf-8")as file:
            reader=csv.reader(file)
            next(reader)
            for row in reader:
                if row[3].upper()==user_input:
                    print(", ".join(row))
                    found=True
        if not found:
            print("No hay juegos con esa clasificacion.")
    except FileNotFoundError:
        print("Archivo no encontrado en:", file_path)

print_pt_csv()                                
