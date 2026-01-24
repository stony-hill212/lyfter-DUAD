import sys
from menu import show_menu,ask_user
from data import students_csv,create_students_csv
from actions import (
    manual_list,
    single_student,
    calculate_averages,
    get_top3,
    calculate_total_ave,
    get_failed_students,
    find_student,
    delete_student
)
def main():
    print("=== Student control system ===")
    option=show_menu()
    while option not in ("1","2"):
        print("Invalid option. Please select 1 or 2.")
        option=show_menu()
    if option=="1":
        students=students_csv()
    elif option=="2":
        students=manual_list()
        create_students_csv(students)
    if not students:
        print("No data available.")
        return
    calculate_averages(students)
    top_students=get_top3(students,top_n=3)
    global_ave=calculate_total_ave(students)
    print("\n---Top 3 students---")
    for student in top_students:
        print(
            f"{student['name']} | "
            f"Section: {student['section']} | "
            f"Average: {student['average']:.2f}"
        )
    print(f"\nClass average: {global_ave:.2f}")
    if ask_user("\nwould you like to see the failed students? (y/n):"):
        failed_students=get_failed_students(students)
        if not student:
                print("student not found.")
        else:
            print(
                    f"Found: {student['name']} | "
                    f"section: {student['section']}"
                )
        if ask_user("are you sure you want to remove this student: (y/n)"):
                    delete_student(students,student)
                    create_students_csv(students)
                    print("removal successful.")
        else:
            print("deletion canceled.")
    if ask_user("\nwould you like to delete a student?(y/n): "):
        while True:
            name=input("Please enter the name of the student: ").strip()
            section=input("\nenter the section: ").strip()
            student=find_student(students,name,section)
            if not student:
                print("student not found.")
                if not ask_user("try again."):
                    break
            else:
                print(f"found: {student['name']} | section {student['section']}")
                if ask_user("are you sure you want to remove this student: (y/n)"):
                    delete_student(students,student)
                    create_students_csv(students)
                    print("student removed")
                else:
                    print("deletion canceled.")
                break
    if option=="1":
        if ask_user("\nWould you like to add another student?(y/n): "):
            new_student=single_student()
            students.append(new_student)
            create_students_csv(students)
            print("student added successfully.")
            
    
if __name__=="__main__":
    main()
    