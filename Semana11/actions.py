def manual_list():
    students=[]
    while True:
        try:
            n=int(input("How many students?: "))
            if n>0:
                break
            print("Number must greater than 0.")
        except ValueError:
            print("please enter a valid number.")
    for i in  range(n):
        print(f"\nEntering the info for student {i+1}")
        name=valid_format("Full name: ")
        section=valid_format("Section (ex: 7B): ")
        english=get_valid_score("English grade: ")
        spanish=get_valid_score("Spanish grade: ")
        history=get_valid_score("History grade: ")
        chemistry=get_valid_score("Chemistry grade: ")
        students.append({
            "name":name,
            "section":section,
            "english":english,
            "spanish":spanish,
            "history":history,
            "chemistry":chemistry,
            "average":None
        })
    return students

def get_valid_score(prompt):
    while True:
        try:
            score=float(input(prompt))
            if 0<=score<=100:
                return score
            print("grade must be between 0 and 100.")
        except ValueError:
            print("Invalid grade.")

def valid_format(prompt):
    while True:
        name=input(prompt).strip()
        if not name:
            print("numbers not allowed in this entry.")
            continue
        stu_name=name.split()
        if all(part.isalpha()for part in stu_name):
            return name
        print("only letters and spaces allowed.")

def empty_spaces(prompt):
    while True:
        value=input(prompt).strip()
        if value:
            return value
        print("No empty spaces.")


def calculate_averages(students):
    for student in students:
        student["average"]=(
            student["english"]
            +student["spanish"]
            +student["history"]
            +student["chemistry"]
        )/4

def get_top3(students,top_n=3):
    sorted_students=sorted(
        students,
        key=lambda s:s["average"],
        reverse=True
    )
    return sorted_students[:top_n]

def calculate_total_ave(students):
    total=sum(student["average"]for student in students)
    return total/len(students)

def get_failed_students(students,passing_grade=60):
    failed=[]
    subjects={
        "english": "English",
        "spanish": "Spanish",
        "history": "History",
        "chemistry": "Chemistry"
    }
    for student in students:
        for key,subject_name in subjects.items():
            grade=student[key]
            if grade<passing_grade:
                failed.append({
                    "name": student["name"],
                    "section": student["section"],
                    "subject": subject_name,
                    "grade": grade
                })
    return failed

def single_student():
    print("\nNew student data:")
    name=valid_format("Full name: ")
    section=empty_spaces("Section: ")
    english=get_valid_score("english grade: ")
    spanish=get_valid_score("spanish grade: ")
    history=get_valid_score("history grade: ")
    chemistry=get_valid_score("chemistry grade: ")
    return{
        "name":name,
            "section":section,
            "english":english,
            "spanish":spanish,
            "history":history,
            "chemistry":chemistry,
            "average":None
    }

def find_student(students,name,section):
    name=name.strip().lower()
    section=section.strip().lower()
    for student in students:
        if(
            student["name"].lower()==name
            and student["section"].lower()==section
        ):
            return student
        return None
    
def delete_student(students,student):
    students.remove(student)