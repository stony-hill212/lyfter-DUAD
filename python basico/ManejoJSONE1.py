import json
import os

base_dir=os.path.dirname(os.path.abspath(__file__))
file_path=os.path.join(base_dir,"pokemon.json")

def show_list(poke_list,extra_attribute=None):
    print("\nPokemon on file:\n")
    for p in poke_list:
        print(p["name"])
        print(f"Type: {', '.join(p['type'])}")
        print(f"HP: {p['base']['HP']}")
        if extra_attribute:
            value=p["base"][extra_attribute]
            reg_name=extra_attribute.replace("-"," ").title()
            print(f"{reg_name}: {value}")
        print()
with open(file_path,"r")as file:
    poke_list=json.load(file)
valid_input={
    key.lower().replace(" ","-"):key
    for key in poke_list[0]["base"].keys()
}
show_list(poke_list)
while True:
    choice=input("Would you like to see another attribute? (y / n): ").lower()
    if choice=="n":
        print("Goodbye.")
        break
    elif choice!="y":
        print("Please enter 'y' or 'n'.")
        continue 
    while True:
        attribute=input("Attribute: ").strip().lower().replace(" ", "-")
        if attribute in valid_input:
            attribute=valid_input[attribute]
            break
        else:
            print("Invalid attribute.")
            print("Valid options:", ", ".join(sorted(valid_input)))
    show_list(poke_list,attribute)