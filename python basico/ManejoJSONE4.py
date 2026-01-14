import json
import os

base_dir=os.path.dirname(os.path.abspath(__file__))
file_path=os.path.join(base_dir,"pokemon.json")

with open(file_path,"r")as file:
    poke_list=json.load(file)
total={}
counter={}
for p in poke_list:
    hp=p["base"]["HP"]
    for t in p["type"]:
        t=t.lower()
        if t not in total:
            total[t]=0
            counter[t]=0
        total[t]+=hp
        counter[t]+=1
print("\nPromedio de nivel:\n")
for t in total:
    average=total[t]/counter[t]
    print(f"Tipo: {t.title()}-Promedio de nivel: {average:.1f}")