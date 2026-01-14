def single_line_txt(current_file,new_file):
    try:
        with open(current_file,"r")as infile:
            words=[]
            for line in infile:
                clean_line=line.strip()
                if clean_line:
                    words.append(clean_line)
        with open(new_file,"w")as outfile:
            outfile.write(" ".join(words))
        print("Archivo convertido correctamente.")    
    except FileNotFoundError:
        print(f"Error: '{input_file}' no se encontro.")
    except PermissionError:
        print("Error: sin acceso.")
    except Exception as e:
        print(f"Error inesperado: {e}")            

from pathlib import Path
base_dir=Path(__file__).parent
input_file=base_dir/"entregableMA.txt"
output_file=base_dir/"nuevoMA.txt"

single_line_txt(input_file,output_file)                    