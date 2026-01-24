import csv
import os

base_dir=os.path.dirname(os.path.abspath(__file__))
file_path=os.path.join(base_dir,"systemControl.csv")

def students_csv():
    students=[]
    if not os.path.exists(file_path):
        print("Error, file not found.")
        return students
    try:
        with open(file_path,newline="",encoding="utf-8")as file:
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
    except KeyError:
        print("Error: CSV file has invalid or missing data.")
    except ValueError:
        print("Error: one or more grades have invalid characters/numbers.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return students

def create_students_csv(students):
    try:
        with open(file_path,"w",newline="",encoding="utf-8")as file:
            user_names=[
                "name",
                "section",
                "english",
                "spanish",
                "history",
                "chemistry"
            ]
            writer=csv.DictWriter(file,fieldnames=user_names)
            writer.writeheader()
            for student in students:
                writer.writerow({
                    "name":student["name"],
                    "section":student["section"],
                    "english":student["english"],
                    "spanish":student["spanish"],
                    "history":student["history"],
                    "chemistry":student["chemistry"]
                })
        print("student data saved to CSV file.")
    except Exception as e:
        print(f"Error: {e}")