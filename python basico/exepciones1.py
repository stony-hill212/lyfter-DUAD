def calculator():
    current_value=0
    while True:
        print("\nCurrent value: ",current_value)
        print("Choose an option: ")
        print("1-Sum")
        print("2-Subtraction")
        print("3-Multiplication")
        print("4-Division")
        print("5-Delete result")
        print("6-Exit")
        selected_option=input("Enter option: ")

        if selected_option=="6":
            print("Exiting program.")
            break
        
        if selected_option=="5":
            current_value=0
            print("result deleted.")
            continue
        
        if selected_option not in{"1","2","3","4"}:
            print("invalid option.")
            continue
        try:
            number=float(input("Enter a number: "))
            if selected_option=="1":
                current_value+=number
            elif selected_option=="2":
                current_value-=number
            elif selected_option=="3":
                current_value*=number
            elif selected_option=="4":
                if number==0:
                    print("Invalid, division by zero not allowed.")
                    continue
                current_value/=number
        except ValueError:
            print("Invalid character, please enter a number.")      


calculator()