def uppercase_file(current_file,new_file):
    try:
        with open(current_file,"r")as target, open(new_file,"w")as destination:
            for line in target:
                destination.write(line.upper())
        print("Archivo creado correctamente.")
    except FileNotFoundError:
        print(f"Error: '{current_file}' no fue encontrado.")
    except PermissionError:
        print("Error: sin accesso.")
    except Exception as e:
        print("Error inesperado: {e}")  

from pathlib import Path
base_dir=Path(__file__).parent
input_file=base_dir/"fighters.txt"
output_file=base_dir/"test1.txt"        

uppercase_file(input_file,output_file)