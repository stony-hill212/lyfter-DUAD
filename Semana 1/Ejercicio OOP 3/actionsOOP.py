from dataOOP import Student
import csv
import os
import re

def valid_grade(target):
    while True:
        try:
            grade=float(input(target))
            if 0<=grade<=100:
                return grade
            print("Please enter a grade between 1-100.")
        except ValueError:
            print("Invalid grade.")

def valid_section():
    while True:
        section=input("Enter the section (ex: 7A): ").strip().upper().replace(" ","")
        if not re.fullmatch(r"\d{1,2}[A-Z]",section):
            print("Invalid format, use a number + a letter.")
            continue
        grade=int(section[:-1])
        letter=section[-1]
        if grade<1 or grade>12:
            print("The number must be between 1-12")
            continue
        if section.startswith("0"):
            print("Zeros are not allowed.")
            continue
        return section

def ask_user(target):
    return input(target).strip().lower() in("y","yes")

def add_student(students):
    name=input("Full name: ").strip()
    section=valid_section()
    if find_student(students,name,section):
        print("Student already exists.")
        return
    english=valid_grade("English grade: ")
    spanish=valid_grade("Spanish grade: ")
    history=valid_grade("History grade: ")
    chemistry=valid_grade("Chemistry grade: ")
    student=Student(
        name=name,
        section=section,
        english=english,
        spanish=spanish,
        history=history,
        chemistry=chemistry
    )
    students.append(student)
    print("Student added to the list.")

def find_student(students,name,section):
    for student in students:
        if student.name.lower()==name.lower()and student.section==section:
            return student
    return None

def delete_student(target):
    name=input("Full name: ").strip()
    section=valid_section("Enter the section: ")
    student=find_student(target,name,section)
    if not student:
        print("Student not found.")
        return
    print(f"Student: {student.name} | Section: {student.section}")
    if ask_user("Are you sure?(y/n): "):
        target.remove(student)
        print("Student deleted.")
    else:
        print("No students removed.")

def all_students(students):
    if not students:
        print("No students available.")
        return
    for s in students:
        print(f"{s.name} | {s.section} | Avg: {s.average:.2f}")

def show_top3(students,top_n=3):
    if not students:
        print("No students available.")
        return
    sorted_students=sorted(students,key=lambda s:s.average,reverse=True)
    for student in sorted_students[:top_n]:
        print(f"{student.name} | {student.section} | Avg: {student.average:.2f}")

def failed_students(target):
    failed=[s for s in target if s.is_failing]
    if not failed:
        print("No failed students.")
        return
    for s in failed:
        print(f"{s.name} | {s.section} | Avg: {s.average:.2f}")

def class_average(target):
    if not target:
        print("No students available.")
        return
    overall=sum(s.average for s in target)/len(target)
    print(f"Overall average: {overall:.2f}")

def export_csv(students,target):
    with open(target,"w",newline="",encoding="utf-8")as file:
        writer=csv.DictWriter(
            file,
            fieldnames=["name","section","english","spanish","history","chemistry"]
        )
        writer.writeheader()
        for student in target:
            writer.writerow(student.to_dict())
    print("Data exported.")

def import_csv(target):
    if not os.path.exists(target):
        print("File not found.")
        return []
    students=[]
    with open(target,"r",newline="",encoding="utf-8")as file:
        reader=csv.DictReader(file)
        for row in reader:
            try:
                students.append(Student.from_dict(row))
            except Exception:
                print("Skipping invalid row.")
    print(f"{len(students)} students imported.")
    return students