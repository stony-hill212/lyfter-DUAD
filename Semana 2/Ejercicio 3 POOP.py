from abc import ABC,abstractmethod

class ProteinSource(ABC):
    @abstractmethod
    def protein_per_100g(self):
        pass
    def calculate_protein(self,weight):
        return(self.protein_per_100g()/100)*weight

class YellowFinTuna(ProteinSource):
    def protein_per_100g(self):
        return 24

class ChickenBreast(ProteinSource):
    def protein_per_100g(self):
        return 31

class Salmon(ProteinSource):
    def protein_per_100g(self):
        return 20

class BeefTenderLoin(ProteinSource):
    def protein_per_100g(self):
        return 26

class Steak(ProteinSource):
    def protein_per_100g(self):
        return 25

class Lentils(ProteinSource):
    def protein_per_100g(self):
        return 9

class TurkeyGroundBeef(ProteinSource):
    def protein_per_100g(self):
        return 27

class Eggs(ProteinSource):
    def protein_per_100g(self):
        return 13

class GreekYogurt(ProteinSource):
    def protein_per_100g(self):
        return 10

def get_valid_weight():
    while True:
        try:
            weight=float(input("Enter weight in grams: "))
            if weight<=0:
                print("Weight must be positive.")
            else:
                return weight
        except ValueError:
            print("Invalid input.")

def get_valid_protein(protein_dict):
    while True:
        choice=input("\nEnter the protein source name (or 'exit'): ").strip().lower()
        if choice=="exit":
            return None
        if choice in protein_dict:
            return protein_dict[choice]
        else:
            print("Invalid protein source, try again.")
            print("Available options:")
            for item in protein_dict:
                print("-",item)

protein_sources={
    "yellowfin tuna":YellowFinTuna(),
    "chicken breast":ChickenBreast(),
    "salmon":Salmon(),
    "beef tenderloin":BeefTenderLoin(),
    "steak":Steak(),
    "lentils":Lentils(),
    "turkey ground beef":TurkeyGroundBeef(),
    "eggs":Eggs(),
    "greek yougurt":GreekYogurt()
}
print("---Protein calculator---")
while True:
    protein_op=get_valid_protein(protein_sources)
    if protein_op is None:
        print("Goodbye.")
        break
    weight=get_valid_weight()
    protein_amount=protein_op.calculate_protein(weight)
    print(f"\nThat amount contains approximately {protein_amount:.2f} grams of protein.\n")