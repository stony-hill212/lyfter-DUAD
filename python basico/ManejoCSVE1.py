import csv
def print_cvsfile(target):
    try:
        with open(target, "r",encoding="utf-8")as file:
            reader=csv.reader(file)
            for row in reader:
                print(" | ".join(row))
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print("Error al leer archivo:", e) 



print_cvsfile("python/juegos1.csv")
