import os

def open_and_print_file_per_line(path):
    with open(path) as file:
        for line in file:
            print(f"Linea: {line.strip()}")

base_dir=os.path.dirname(__file__)
file_path=os.path.join(base_dir, "Chuck Lidell.txt")

open_and_print_file_per_line(file_path)
