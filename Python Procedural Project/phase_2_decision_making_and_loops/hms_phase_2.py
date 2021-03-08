import os


staff1 = ''
staff2 = ''
staff3 = ''
staff1pass = ''
staff2pass = ''
staff3pass = ''
user1 = ''
user2 = ''
user3 = ''
user1pass = ''
user2pass = ''
user3pass = ''
user1att = 0
user2att = 0
user3att = 0
user1fees = ''
user2fees = ''
user3fees = ''
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
                            if staff1 == '':
                                staff = input("Enter name for new staff: ")
                                staff1pass = input("Enter password for new staff: ")
                            elif staff2 == '':
                                staff2 = input("Enter name for new staff: ")
                                staff2pass = input("Enter password for new staff: ")
                            elif staff3 == '':
                                staff3 = input("Enter name for new staff: ")
                                staff3pass = input("Enter password for new staff: ")
                            else:
                                input(
                                    "Maximum User capacity has been reached\nPress ENTER to continue...")
                    if choice == '2':
                        name = input("Enter user name: ")
                        if name == user1:
                            user1 = ''
                            user1pass = ''
                            input(
                                name, "Removed successfully\nPress ENTER to continue...")
                        elif name == user2:
                            user2 = ''
                            user2pass = ''
                            input(
                                name, "Removed successfully\nPress ENTER to continue...")
                        elif name == user3:
                            user3 = ''
                            user3pass = ''
                            input(
                                name + " removed successfully\nPress ENTER to continue...")
                        else:
                            input("User not found\nPress ENTER to continue...")
                    if choice == '3':
                        expenses += int(input("Enter the expenses: "))
                        input("\nPress ENTER to continue...")
                    if choice == '4':
                        print("The total expenses are:", (user1att * 50 + user2att * 50 + user3att * 50) + expenses)
                        input("\nPress ENTER to continue...")
                    if choice == '5':
                        print("Name\tPassword")
                        if user1 != '':
                            print(user1, user1pass, sep='\t')
                        if user2 != '':
                            print(user2, user2pass, sep='\t')
                        if user3 != '':
                            print(user3, user3pass, sep='\t')
                        input("\nPress ENTER to continue...")
                    if choice == '6':
                        print("Name\tFees")
                        if user1 != '':
                            print(user1, user1att * 50, sep='\t')
                        if user2 != '':
                            print(user2, user2att * 50, sep='\t')
                        if user3 != '':
                            print(user3, user3att * 50, sep='\t')
                        input("\nPress ENTER to continue...")
                    if choice == '7':
                        in_admin = False
                        input("Logging out\nPress ENTER to continue...")
                input("\nPress ENTER to continue...")
            else:
                input("Invalid name or password\nPress ENTER to continue...")
        
        elif choice == '2':
            name = input("Enter user name: ")
            password = input("Enter user password: ")

            if name == user1 and password == user1pass:
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
                        print("This month's total bill is: ", user1att * 50)
                    elif choice == '2':
                        print("This month's total attendance is: ", user1att)
                    elif choice == '3':
                        in_user = False
            elif name == user2 and password == user2pass:
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
                        print("This month's total bill is: ", user2att * 50)
                        input("\nPress ENTER to continue...")
                    elif choice == '2':
                        print("This month's total attendance is: ", user2att)
                        input("\nPress ENTER to continue...")
                    elif choice == '3':
                        in_user = False
            elif name == user3 and password == user3pass:
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
                        print("This month's total bill is: ", user3att * 50)
                        input("\nPress ENTER to continue...")
                    elif choice == '2':
                        print("This month's total attendance is: ", user3att)
                        input("\nPress ENTER to continue...")
                    elif choice == '3':
                        in_user = False
        elif choice == '3':
            name = input("Enter staff name: ")
            password = input("Enter staff password: ")

            if name == staff1 and password == staff1pass:
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
                        if user1 != '':
                            print(user1)
                        if user2 != '':
                            print(user2)
                        if user3 != '':
                            print(user3)
                            input("\nPress ENTER to continue...")
                    elif choice == '2':
                        name = input("Enter user name: ")
                        if name == user1:
                            user1att = int(input("Enter user attendence: "))
                        elif name == user2:
                            user1att = int(input("Enter user attendence: "))
                        elif name == user3:
                            user1att = int(input("Enter user attendence: "))
                        else:
                            input("Username not found!\nPress any key to continue...")
                        input("\nPress ENTER to continue...")
                    elif choice == '3':
                        in_user = False
            elif name == staff2 and password == staff2pass:
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
                        if user1 != '':
                            print(user1)
                        if user2 != '':
                            print(user2)
                        if user3 != '':
                            print(user3)
                        input("\nPress ENTER to continue...")
                    elif choice == '2':
                        name = input("Enter user name: ")
                        if name == user1:
                            user1att = int(input("Enter user attendence: "))
                        elif name == user2:
                            user1att = int(input("Enter user attendence: "))
                        elif name == user3:
                            user1att = int(input("Enter user attendence: "))
                        else:
                            input("Username not found!\nPress any key to continue...")
                        input("\nPress ENTER to continue...")
                    elif choice == '3':
                        in_user = False
            elif name == staff3 and password == staff3pass:
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
                        if user1 != '':
                            print(user1)
                        if user2 != '':
                            print(user2)
                        if user3 != '':
                            print(user3)
                        input("\nPress ENTER to continue...")
                    elif choice == '2':
                        name = input("Enter user name: ")
                        if name == user1:
                            user1att = int(input("Enter user attendence: "))
                        elif name == user2:
                            user1att = int(input("Enter user attendence: "))
                        elif name == user3:
                            user1att = int(input("Enter user attendence: "))
                        else:
                            input("Username not found!\nPress any key to continue...")
                        input("\nPress ENTER to continue...")
                    elif choice == '3':
                        in_user = False
    if choice == '2':
        in_menu = False