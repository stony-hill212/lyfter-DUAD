from menuOOP import show_menu,get_menu
from actionsOOP import(
    add_student,
    all_students,
    show_top3,
    class_average,
    failed_students,
    delete_student,
    export_csv,
    import_csv
)
def main():
    students=[]
    while True:
        show_menu()
        option=get_menu(1,9)
        if option==1:
            add_student(students)
        elif option==2:
            all_students(students)
        elif option==3:
            show_top3(students)
        elif option==4:
            class_average(students)
        elif option==5:
            failed_students(students)
        elif option==6:
            delete_student(students)
        elif option==7:
            export_csv(students)
        elif option==8:
            imported_students=import_csv()
            if imported_students:
                students.extend(imported_students)
        elif option==9:
            print("Exiting program.")
            break

if __name__=="__main__":
    main()