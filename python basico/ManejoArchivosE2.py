def count_words(myfile):
    try:
        word_count=0
        with open(myfile,"r")as target:
            for line in target:
                words_f_file=line.split()
                word_count+=len(words_f_file)
        print(f"Este archivo tiene {word_count} palabras.")
    except FileNotFoundError:
        print(f"Error: '{myfile}' no se encontro.")
    except PermissionError:
        print(f"Error: sin acceso.") 
    except Exception as e:
        print(f"Error inesperado: {e}")

from pathlib import Path
base_dir=Path(__file__).parent
input_file=base_dir/"fighters.txt"

count_words(input_file)                           
