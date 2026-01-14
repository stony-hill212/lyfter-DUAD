import json
import os

base_dir=os.path.dirname(os.path.abspath(__file__))
file_path=os.path.join(base_dir,"pokemon.json")
def get_duplicate(poke_list,name):
    name=name.lower()
    for p in poke_list:
        if p["name"].lower()==name:
            return True
    return False
    
def get_valid(target):
    while True:    
        try:
            return int(input(target))
        except ValueError:
            print("Invalid input, please enter a number.")
if not os.path.exists(file_path):
    poke_list=[] 
else:
    try:
        with open(file_path,"r")as file:
            poke_list=json.load(file)
    except json.JSONDecodeError:
        print("JSON file empty or corrupted.")
        poke_list=[]
if poke_list:
    print("Pokemon in the file: ")
    for p in poke_list:
        print("-", p["name"])
else:
    print("No pokemon found.")

while True:
    choice=input("\nAdding a new pokemon?(y/n): ").lower()
    if choice=="y":
        pass
    elif choice=="n":
        print("Goodbye.")
        break
    else:
        print("Please enter 'y' or 'n'.")
        continue 
    while True:
        name=input("Enter a pokemon name: ").strip()
        if get_duplicate(poke_list,name):
            print("That pokemon is already on file.")
        else:
            break
    new_pokemon={
    "name":name,
    "type":[input("Enter pokemon type: ")],
    "base":{
        "HP":get_valid("HP: "),
        "Attack":get_valid("Attack: "),
        "Defense":get_valid("Defense: "),
        "sp_attack":get_valid("Sp. Attack: "),
        "sp_defense":get_valid("Sp. defense: "),
        "Speed":get_valid("Speed: ")
    }
}
    poke_list.append(new_pokemon)
    with open(file_path,"w")as file:
        json.dump(poke_list,file,indent=4)
    print("\nPokemon added successfully.") 

        

    