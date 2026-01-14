import json
import os

base_dir=os.path.dirname(os.path.abspath(__file__))
file_path=os.path.join(base_dir,"pokemon.json")
with open(file_path,"r")as file:
    poke_list=json.load(file)
valid_input={t.lower()for p in poke_list for t in p["type"]}
while True:
    user_input=input("Ingrese el tipo de pokemon que desea buscar(fire, water, electric.): ").strip().lower()
    if user_input in valid_input:
        break
    else:
        print("tipo invalido.")
        print("opciones disponibles:", ", ".join(sorted(valid_input)))
print("\nLos pokemon que existen de ese tipo son: ")
selected=False
for p in poke_list:
    poke_type=[t.lower()for t in p["type"]]
    if user_input in poke_type:
        print(p["name"])
        selected=True
if not selected:
    print("Ninguno de ese tipo.")
