from abc import ABC,abstractmethod
import json

class Food(ABC):
    @abstractmethod
    def protein_per_100g(self):
        pass
    @abstractmethod
    def calories_per_100g(self):
        pass
    @abstractmethod
    def fat_per_100g(self):
        pass
    @abstractmethod
    def carbs_per_100g(self):
        pass
    def calculate_macros(self,weight):
        factor=weight/100
        return{
            "protein":self.protein_per_100g()*factor,
            "calories":self.calories_per_100g()*factor,
            "fat":self.fat_per_100g()*factor,
            "carbs":self.carbs_per_100g()*factor
        }

class ChickenBreast(Food):
    def protein_per_100g(self):return 31
    def calories_per_100g(self):return 165
    def fat_per_100g(self):return 3.6
    def carbs_per_100g(self):return 0

class Salmon(Food):
    def protein_per_100g(self):return 20
    def calories_per_100g(self):return 208
    def fat_per_100g(self):return 13
    def carbs_per_100g(self):return 0

class Lentils(Food):
    def protein_per_100g(self):return 9
    def calories_per_100g(self):return 116
    def fat_per_100g(self):return 0.4
    def carbs_per_100g(self):return 20

class Steak(Food):
    def protein_per_100g(self):return 25
    def calories_per_100g(self):return 271
    def fat_per_100g(self):return 19
    def carbs_per_100g(self):return 0

class BaseTracker:
    def __init__(self):
        self.days={}
        self.current_day="Day 1"
        self.days[self.current_day]=self._empty_day()
    def _empty_day(self):
        return{
            "protein":0,
            "calories":0,
            "fat":0,
            "carbs":0
        }
    def add_macros(self,macros):
        for mac in macros:
            self.days[self.current_day][mac]+=macros[mac]
    def show_summary(self):
        print(f"\n==={self.current_day} Summary ===")
        for k,v in self.days[self.current_day].items():
            print(f"{k.capitalize()}: {v:.2}")

class GoalMixin:
    def set_protein_goal(self,goal):
        self.protein_goal=goal
    def show_goal_progress(self):
        protein=self.days[self.current_day]["protein"]
        percent=(protein/self.protein_goal)*100 if self.protein_goal else 0
        print(f"\nProtein goal: {protein:.2f}/{self.protein_goal}g, {percent:.1f}%")

class PersistenceMixin:
    def save_to_file(self,filename="diet_tracker.json"):
        with open(filename,"w")as f:
            json.dump(self.days,f,indent=4)
    def load_from_file(self,filename="diet_tracker.json"):
        try:
            with open(filename,"r")as f:
                self.days=json.load(f)
        except FileNotFoundError:
            print("No saved data found.")

class UnitConversionMixin:
    @staticmethod
    def grams_to_oz(grams):
        return grams/28.3495
    @staticmethod
    def oz_to_grams(oz):
        return oz*28.3495

class AdvancedTracker(BaseTracker,GoalMixin,PersistenceMixin,UnitConversionMixin):
    pass

def get_valid_weight():
    while True:
        try:
            weight=float(input("Enter weight: "))
            if weight<=0:
                print("Weight must be positive.")
                continue
            unit=input("Unit?(g/oz): ").strip().lower()
            if unit not in ["g","oz"]:
                print("Invalid unit.")
                continue
            if unit=="oz":
                weight=AdvancedTracker.oz_to_grams(weight)
            return weight
        except ValueError:
            print("Invalid number.")

def get_food_choice(food_dict):
    while True:
        choice=input("\nEnter the food (or summary/save/load/exit): ").strip().lower()
        if choice in ["exit","summary","save","load"]:
            return choice
        if choice in food_dict:
            return food_dict[choice]
        print("Invalid option, available choices:")
        for food in food_dict:
            print("-",food)

foods={
    "chicken breast":ChickenBreast(),
    "salmon":Salmon(),
    "lentils":Lentils(),
    "steak":Steak()
}
tracker=AdvancedTracker()
goal_input=float(input("Enter daily protein goal (grams): "))
tracker.set_protein_goal(goal_input)
print("\n===Diet macro tracker===")
while True:
    selection=get_food_choice(foods)
    if selection=="exit":
        print("Goodbye.")
        break
    if selection=="summary":
        tracker.show_summary()
        tracker.show_goal_progress()
        continue
    if selection=="save":
        tracker.save_to_file()
        print("Data saved.")
        continue
    if selection=="load":
        tracker.load_from_file()
        print("Data loaded.")
        continue
    weight=get_valid_weight()
    macros=selection.calculate_macros(weight)
    tracker.add_macros(macros)
    print("\nAdded:")
    for k,v in macros.items():
        print(f"{k.capitalize()}: {v:.2f}")
    
    tracker.show_goal_progress()
