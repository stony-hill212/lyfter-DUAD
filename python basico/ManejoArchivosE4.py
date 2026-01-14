def append_to_file(my_file):
    try:
        user_entry=input("Ingrese una linea de texto: ")
        with open(my_file,"a")as file:
            file.write(user_entry+"\n")
        print("Linea agregada.")
    except FileNotFoundError:
        print(f"Error: '{my_file}' no fue encontrado.")
    except PermissionError:
        print("Error: sin accesso.")
    except Exception as e:
        print("Error inesperado: {e}")

from pathlib import Path
base_dir=Path(__file__).parent
input_file=base_dir/"nuevoMA.txt"        

append_to_file(input_file)
