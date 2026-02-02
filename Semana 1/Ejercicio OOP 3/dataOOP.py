import csv
import os

class Student:
    def __init__(self,name,section,english,spanish,history,chemistry):
        self.name=name
        self.section=section
        self.english=english
        self.spanish=spanish
        self.history=history
        self.chemistry=chemistry

    @property
    def average(self):
        return(
            self.english+
            self.spanish+
            self.history+
            self.chemistry
        )/4
    
    def to_dict(self):
        return{
            "name":self.name,
            "section":self.section,
            "english":self.english,
            "spanish":self.spanish,
            "history":self.history,
            "chemistry":self.chemistry
        }
    
    @staticmethod
    def from_dict(target):
        return Student(
            name=target["name"].strip(),
            section=target["section"].strip().upper(),
            english=float(target["english"]),
            spanish=float(target["spanish"]),
            history=float(target["history"]),
            chemistry=float(target["chemistry"])
        )

def import_students(target):
    students=[]
    if not os.path.exists(target):
        print("File not found.")
        return students
    try:
        with open(target,mode="r",newline="",encoding="utf-8")as file:
            reader=csv.DictReader(file)
            for row in reader:
                if any(not row[key]for key in["name","section","english","spanish","history","chemistry"]):
                    continue
                try:
                    student=Student.from_dict(row)
                    students.append(student)
                except ValueError:
                    continue
        return students
    except Exception as e:
        print(f"Error: {e}")
        return []
    
def export_students(students,target):
    try:
        with open(target,mode="w",newline="",encoding="utf-8",)as file:
            spaces=["name","section","english","spanish","history","chemistry"]
            writer=csv.DictWriter(file,fieldnames=spaces)
            writer.writeheader()
            for student in students:
                writer.writerow(student.to_dict())
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False