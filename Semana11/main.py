from menu import show_menu
from actions import(
    add_student,
    show_students,
    show_top3,
    class_average,
    failed_students,
    delete_student
)
from data import import_csv,save_to_csv

def main():
    students=[]
    while True:
        option=show_menu()
        if option=="1":
            add_student(students)
        elif option=="2":
            show_students(students)
        elif option=="3":
            show_top3(students)
        elif option=="4":
            class_average(students)
        elif option=="5":
            failed_students(students)
        elif option=="6":
            delete_student(students)
        elif option=="7":
            select_file=input("Enter the name of the file to export (ex: systemControl.csv): ").strip()
            save_to_csv(students,select_file)
            print("Data exported successfully.")
        elif option=="8":
            select_file=input("Enter the name of the file to import (ex: systemControl.csv): ").strip()
            imported=import_csv(select_file)
            if imported:
                students.extend(imported)
                print(f"{len(imported)} student(s) imported.")
            else:
                print("No data imported.")
        elif option=="9":
            print("Exiting program.")
            break
        else:
            print("Invalid option, please enter a number from 1-9.")

if __name__=="__main__":
    main()

    
