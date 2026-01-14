import json
import os

base_dir=os.path.dirname(os.path.abspath(__file__))
file_path=os.path.join(base_dir,"pokemon.json")

with open(file_path,"r")as file:
    poke_list=json.load(file)
print("\nEstadisticas principales:\n")
for p in poke_list:
    print(f"Nombre: {p['name']}")
    print(f"Ataque: {p['base']['Attack']}")
    print(f"Defensa: {p['base']['Defense']}")
    print(f"Velocidad: {p['base']['Speed']}")
    print()
