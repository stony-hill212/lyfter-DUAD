import csv
import os

base_dir=os.path.dirname(os.path.abspath(__file__))
file_path=os.path.join(base_dir,"systemControl.csv")

def import_csv(target):
    students=[]
    if not os.path.exists(target):
        print("Error, file not found.")
        return students
    try:
        with open(target,mode="r",newline="",encoding="utf-8")as file:
            reader=csv.DictReader(file)
            for row in reader:
                student={
                    "name":row["name"],
                    "section":row["section"],
                    "english":float(row["english"]),
                    "spanish":float(row["spanish"]),
                    "history":float(row["history"]),
                    "chemistry":float(row["chemistry"]),
                    "average":None 
            }
                students.append(student)
        return students
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def save_to_csv(students,target):
    try:
        with open(target,mode="w",newline="",encoding="utf-8")as file:
            fields=["name","section","english","spanish","history","chemistry"]
            writer=csv.DictWriter(file,fieldnames=fields)
            writer.writeheader()
            for student in students:
                writer.writerow(student)
    except Exception as e:
        print(f"Error saving file: {e}")

