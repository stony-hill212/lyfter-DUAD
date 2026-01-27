import re

def valid_name(target):
    while True:
        name=input(target).strip()
        if not name:
            print("Filed cannot be empty.")
            continue
        elif any(char.isdigit() for char in name):
            print("Name cannot contain numbers.")
            continue
        return name.title()
    
def valid_section():
    while True:
        section=input("Enter the section (ex: 7A): ").strip().lower().replace(" ","")
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

def valid_grade(subject):
    while True:
        value=input(f"Enter {subject} grade (0-100): ").strip()
        try:
            grade=float(value)
            if 0<=grade<=100:
                return grade
            else:
                print("Grade must be between 1-100.")
        except ValueError:
            print("Invalid number.")

def duplicate_student(students,name,section):
    for s in students:
        if s["name"].lower()==name.lower() and s["section"]==section:
            return True
    return False

def add_student(students):
    print("\n--- Add student ---")
    name=valid_name("Full name: ")
    section=valid_section()
    if duplicate_student(students,name,section):
        print("This student already exists in this section.")
        return
    english=valid_grade("English")
    spanish=valid_grade("Spanish")
    history=valid_grade("History")
    chemistry=valid_grade("Chemistry")
    student={
        "name":name,
        "section":section,
        "english":english,
        "spanish":spanish,
        "history":history,
        "chemistry":chemistry
    }
    students.append(student)
    print("Student added to file.")

def show_students(target):
    if not target:
        print("No students available.")
        return
    print("\n--- All students ---")
    for s in target:
        print(f"{s['name']} | Section {s['section']} | "
            f"E:{s['english']} S:{s['spanish']} H:{s['history']} C:{s['chemistry']}")

def calculate_average(target):
    return(target["english"]+target["spanish"]+target["history"]+target["chemistry"])/4

def show_top3(target):
    if len(target)<3:
        print("Not enough students at the moment, please add more info later.")
        return
    sorted_students=sorted(target,key=lambda s:calculate_average(s),reverse=True)
    print("\n---top 3 students---")
    for s in sorted_students[:3]:
        avg=calculate_average(s)
        print(f"{s['name']} | Section {s['section']} | Average: {avg:.2f}")

def class_average(target):
    if not target:
        print("No students available.")
        return
    total=sum(calculate_average(s)for s in target)
    overall=total/len(target)
    print(f"\nClass grade average: {overall:.2f}")

def failed_students(target):
    print("\n---Failed students---")
    found=False
    for s in target:
        for subject in["english","spanish","history","chemistry"]:
            if s[subject]<60:
                print(f"{s['name']} | Section {s['section']} | Failed {subject.capitalize()} ({s[subject]})")
                found=True
    if not found:
        print("No failed students.")

def delete_student(target):
    if not target:
        print("No students to delete.")
        return
    name=input("Enter student's full name to delete: ").strip()
    section=input("Enter section: ").strip().upper().replace(" ","")
    for s in target:
        if s["name"].lower()==name.lower()and s["section"]==section:
            print(f"Found: {s['name']} | Section {s['section']}")
            confirm=input("Are you sure you want to delete? (y/n): ").strip().lower()
            if confirm in["y","yes"]:
                target.remove(s)
                print("Student deleted.")
            else:
                print("No students deleted.")
                return
    print("Student not found.")
