def sort_names(input_file,output_file):
    with open(input_file,"r",encoding="utf-8") as f:
        names=[line.strip()for line in f if line.strip()]
        names.sort(key=str.lower)

    with open(output_file,"w",encoding="utf-8")as f:
        for name in names:
            f.write(name+"\n")   

from pathlib import Path
BASE_DIR=Path(__file__).parent
input_file=BASE_DIR/"songs.txt"
output_file=BASE_DIR/"sorted_names.txt"

sort_names(input_file,output_file)