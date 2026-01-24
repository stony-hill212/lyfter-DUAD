def show_menu():
    print("\nChoose an option:")
    print("1 - Import names and data from CSV file")
    print("2 - Enter the data manually")
    option=input("Enter option 1 or 2: ").strip()
    return option

def ask_user(prompt):
    while True:
        choice=input(prompt).strip().lower()
        if choice in("y","yes"):
            return True
        elif choice in("n","no"):
            return False
        print("Invalid input, please enter y/yes or n/no.")