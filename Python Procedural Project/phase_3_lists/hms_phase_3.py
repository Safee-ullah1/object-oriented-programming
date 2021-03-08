import os


staff_names = []
staff_passwords = []
user_names = []
user_passwords = []
user_atts = []
expenses = 0

admin_name = "admin"
admin_pass = "1234"
in_menu = True
while in_menu:
    os.system("cls")
    print("\n\t\tMain Menu > ",
          "\n\t--------- --------- -------- -------- -------- -------- -------- -------- --------- --------",
          "1. Login",
          "2. Exit", sep='\n')
    choice = input("\nEnter your choice: ")
    if choice == '1':
        os.system("cls")
        print("\n\t\tMain Menu > Login > ",
              "\n\t--------- --------- -------- -------- -------- -------- -------- -------- --------- --------\n\t\tLogin as:\n",
              "1. Administrator",
              "2. Resident",
              "3. Staff",
              "4. Go back", sep='\n')
        choice = input("\nEnter your choice: ")
        if choice == '1':
            name_in = input("\nEnter admin name: ")
            pass_in = input("Enter admin password: ")
            if name_in == admin_name and pass_in == admin_pass:
                in_admin = True
                while in_admin:
                    os.system("cls")
                    print("\n\t\tMain Menu > Login > Admin > ",
                          "\n\t--------- --------- -------- -------- -------- -------- -------- -------- --------- --------\n\t\tChoose option:\n",
                          "1. Add a user",
                          "2. Remove a user",
                          "3. Add expenses",
                          "4. Calculate expenses",
                          "5. View all members",
                          "6. View resident fees",
                          "7. Logout", sep='\n')
                    choice = input("\nEnter your choice: ")
                    if choice == '1':
                        print("1. Add staff",
                              "2. Add resident",
                              sep='\n')
                        choice = input("\nYour choice: ")
                        if choice == '1':
                            staff = input("Enter name for new staff: ")
                            staff_pass = input("Enter password for new staff: ")
                            staff_names.append(staff)
                            staff_passwords.append(staff_pass)
                        elif choice == '2':
                            user = input("Enter name for new user: ")
                            user_pass = input("Enter password for new user: ")
                            user_names.append(user)
                            user_passwords.append(user_pass)
                            user_atts.append(0)
                    elif choice == '2':
                        name = input("Enter user name: ")
                        if name in user_names:
                            idx = user_names.index(name)
                            user_names.remove(idx)
                            user_passwords.remove(idx)
                            user_atts.remove(idx)
                        else:
                            input("Username not found!\nPress any key to continue...")
                    elif choice == '3':
                        expenses += int(input("Enter the expenses: "))
                        input("\nPress ENTER to continue...")
                    elif choice == '4':
                        total = 0
                        for attendence in user_atts:
                            total += attendence * 50
                        print("The total expenses are:", total)
                        input("\nPress ENTER to continue...")
                    elif choice == '5':
                        print("Name\tPassword")
                        for user, password in zip(user_names, user_passwords):
                            print(user, password, sep='\t')
                        input("\nPress ENTER to continue...")
                    elif choice == '6':
                        print("Name\tFees")
                        for user, attendance in zip(user_names, user_atts):
                            print(user, attendance, sep='\t')
                        input("\nPress ENTER to continue...")
                    elif choice == '7':
                        in_admin = False
                        input("Logging out\nPress ENTER to continue...")
                input("\nPress ENTER to continue...")
            else:
                input("Invalid name or password\nPress ENTER to continue...")
        
        elif choice == '2':
            name = input("Enter user name: ")
            password = input("Enter user password: ")
            if name in user_names:
                idx = user_names.index(name)
                if password == user_passwords[idx]:
                    in_user = True
                    while in_user:
                        os.system("cls")
                        print("\n\t\tMain Menu > Login > Resident > ",
                            "\n\t--------- --------- -------- -------- -------- -------- -------- -------- --------- --------\n\t\tChoose option:\n",
                            "1. View this month\'s bill",
                            "2. View attendance",
                            "3. logout", sep='\n')
                        choice = input("\nEnter your choice: ")
                        if choice == '1':
                            print("This month's total bill is: ", user_atts[idx] * 50)
                        elif choice == '2':
                            print("This month's total attendance is: ", user_atts[idx])
                        elif choice == '3':
                            in_user = False
                        input("\nPress any key to continue...")
        elif choice == '3':
            name = input("Enter staff name: ")
            password = input("Enter staff password: ")
            
            if name in staff_names:
                idx = staff_names.index(name)
                if password == staff_passwords[idx]:
                    in_user = True
                    while in_user:
                        os.system("cls")
                        print("\n\t\tMain Menu > Login > Staff > ",
                            "\n\t--------- --------- -------- -------- -------- -------- -------- -------- --------- --------\n\t\tChoose option:\n",
                            "1. View all Residents",
                            "2. Add Attendance",
                            "3. Logout", sep='\n')
                        choice = input("\nEnter your choice: ")
                        if choice == '1':
                            print("Name: ")
                            for user_name in user_names:
                                print(user_name)
                        elif choice == '2':
                            name = input("Enter user name: ")
                            if name in user_names:
                                user_atts[user_names.index(name)] = int(input("Enter user attendence: "))
                            else:
                                input("Username not found!\nPress any key to continue...")
                            input("\nPress ENTER to continue...")
                        elif choice == '3':
                            in_user = False
                        input("\nPress ENTER to continue...")
    elif choice == '2':
        in_menu = False