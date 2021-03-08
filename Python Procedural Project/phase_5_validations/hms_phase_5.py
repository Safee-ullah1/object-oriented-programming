import os

staff_names = []
staff_passwords = []
user_names = []
user_passwords = []
user_atts = []
notices = []
applications = []
fees = []
expenses = 0
sorted_indexes = []
sorted_fees = []
sorted_names = []
admin_pass = "1234"


def main():
    load_demo_data()
    while True:
        os.system("cls")
        display_header()
        option = display_menu(get_menu_items("main"))
        if option == '1':
            login_option = '-1'
            while login_option != '4':
                os.system("cls")
                display_header()
                login_option = display_menu(get_menu_items("login"))
                if login_option == '1':  # Admin
                    pass_check = input("\n\nEnter Password: ")
                    if pass_check == admin_pass:
                        admin_option = '-1'
                        while admin_option != '12':  # Admin menu loop
                            os.system("cls")
                            display_header()
                            admin_option = display_menu(
                                get_menu_items("admin"))
                            if admin_option == '1':  # Adding User
                                add_option = display_menu(
                                    get_menu_items("add"))
                                if add_option == '1':
                                    add_staff_ui()
                                    wait("")
                                elif add_option == '2':
                                    add_resident_ui()
                                    wait("")
                                elif add_option == '3':
                                    wait("")
                            elif admin_option == '2':  # Removing User
                                removing_option = display_menu(
                                    get_menu_items("remove"))
                                if removing_option == '1':
                                    name = input("\n\nEnter User Name: ")
                                    remove_member("staff", name)
                                    wait("")
                                elif removing_option == '2':
                                    name = input("\n\nEnter User Name: ")
                                    remove_member("resident", name)
                                    wait("")
                                elif removing_option == '3':
                                    wait("")
                            elif admin_option == '3':  # View all apllications
                                view_applications()
                                wait("")

                            elif admin_option == '4':  # Remove Application
                                remove_application()
                                wait("")

                            elif admin_option == '5':  # Add expenses
                                expenses = int(input("\n\t\tEnter expenses: "))
                                if expenses >= 0 and expenses <= 100000:
                                    print("This month's expenses are: ", expenses)
                                else:
                                    print("Invalid amount entered. Please retry")
                                wait("")

                            elif admin_option == '6':  # Calculate expenses
                                calculate_fees()
                                wait("")

                            elif admin_option == '7':  # View expenses
                                print("This month's expenses are: ", expenses)
                                wait("")
                            elif admin_option == '8':  # Make a notice on the notice board
                                add_notice_ui()
                                wait("")
                            elif admin_option == '9':  # Display notices
                                show_notices()
                                wait("")
                            elif admin_option == '10':  # View all members
                                display_members(
                                    "Staff", staff_names, staff_passwords)
                                display_members(
                                    "Residents", user_names, user_passwords)
                                wait("")
                            elif admin_option == '11':  # View resident fees
                                calculate_fees()
                                sort()
                                display_ordered_residents()
                                wait("")
                            elif admin_option == '12':  # Logout
                                wait("")
                    else:
                        print("\nInvalid Password!!")
                        wait("")

                elif login_option == '2':  # Resident
                    name = input("Enter username: ")
                    password = input("Enter password: ")
                    logi = login(user_names, user_passwords, name, password)
                    if logi:
                        while logi:
                            os.system("cls")
                            display_header()
                            resident_option = '-1'
                            user_idx = user_names.index(name)
                            resident_option = display_menu(
                                get_menu_items("resident"))
                            if resident_option == '1':  # Bill for current month
                                calculate_fees()
                                print(
                                    "\nYour Bill for the Current Month is: ", fees[user_idx])
                                wait("")

                            elif resident_option == 2:  # Attendance for the Current Month
                                print(
                                    "\nYour Attendance for the Current Month is: ", user_atts[user_idx])
                                wait("")

                            elif resident_option == 3:  # Logout
                                logi = False
                                wait("")
                    else:
                        wait("")
                elif login_option == 3:  # Staff
                    name = input("Enter username: ")
                    password = input("Enter password: ")
                    logi = login(staff_names, staff_passwords, name, password)
                    if logi:
                        while logi:
                            os.system("cls")
                            display_header()
                            staff_option = '-1'
                            user_idx = staff_names.index(name)
                            staff_option = display_menu(
                                get_menu_items("staff"))
                            if staff_option == '1':  # Display members
                                display_members(
                                    "residents", user_names, user_passwords)
                                wait("")
                            elif staff_option == '2':  # Add attendance
                                add_attendance_ui()
                                wait("")
                            elif staff_option == '3':  # logout
                                login = False
                                wait("")
                    else:
                        wait("")
                elif login_option == '4':  # go back
                    wait("")
        elif option == '2':  # View Notice Board
            show_notices()
            wait("")
        elif option == '3':  # Apply for Allotment
            make_application()
            wait("")
        elif option == 4:  # View application status
            check_status()
            wait("")
        elif option == 5:  # Close program
            print("\n\t\tThank you for using the software,")
            wait("")


def display_header():
    header = ["                          __  __           __       __",
              "                         / / / /___  _____/ /____  / /",
              "                        / /_/ / __ \\/ ___/ __/ _ \\/ /",
              "                       / __  / /_/ (__  ) /_/  __/ /",
              "                      /_/ /_/\\____/____/\\__/\\___/_/",
              "           __  ___                                                  __",
              "          /  |/  /___ _____  ____ _____ ____  ____ ___  ___  ____  / /_",
              "         / /|_/ / __ `/ __ \\/ __ `/ __ `/ _ \\/ __ `__ \\/ _ \\/ __ \\/ __/",
              "        / /  / / /_/ / / / / /_/ / /_/ /  __/ / / / / /  __/ / / / /_",
              "       /_/  /_/\\__,_/_/ /_/\\__,_/\\__, /\\___/_/ /_/ /_/\\___/_/ /_/\\__/",
              "                                /____/",
              "                      _____            __",
              "                     / ___/__  _______/ /____  ____ ___",
              "                     \\__ \\/ / / / ___/ __/ _ \\/ __ `__ \\  ",
              "                    ___/ / /_/ (__  ) /_/  __/ / / / / /",
              "                   /____/\\__, /____/\\__/\\___/_/ /_/ /_/",
              "                        /____/ "]
    for line in header:
        print(line)


def display_menu(menu):
    for item in menu:
        print(item)
    selection = input("\nYour Choice: ")
    return selection


def get_menu_items(menu_name):
    menu_names = ["main", "login", "admin",
                  "resident", "staff", "add", "remove"]
    menus = [[
        "\n\t\tMain Menu > ",
        "\n\t--------- --------- -------- -------- -------- -------- -------- -------- --------- --------",
        "1. Login",
        "2. View Notice Board",
        "3. Apply for Allotment/Employment",
        "4. View status",
        "5. Exit"
    ], [
        "\n\t\tMain Menu > Login > ",
        "\n\t--------- --------- -------- -------- -------- -------- -------- -------- --------- --------\n\t\tLogin as:\n",
        "1. Administrator",
        "2. Resident",
        "3. Staff",
        "4. Go back"
    ], [
        "\n\t\tMain Menu > Login > Admin > ",
        "\n\t--------- --------- -------- -------- -------- -------- -------- -------- --------- --------\n\t\tChoose option:\n",
        "1. Add a user",
        "2. Remove a user",
        "3. View applications",
        "4. Remove applications",
        "5. Add expenses",
        "6. Calculate expenses",
        "7. View this month\'s expenses",
        "8. Make a notice on the notice board",
        "9. View Notice board",
        "10. View all members",
        "11. View resident fees",
        "12. Logout"
    ], [
        "\n\t\tMain Menu > Login > Resident > ",
        "\n\t--------- --------- -------- -------- -------- -------- -------- -------- --------- --------\n\t\tChoose option:\n",
        "1. View this month\'s bill",
        "2. View attendance",
        "3. logout"
    ], [
        "\n\t\tMain Menu > Login > Staff > ",
        "\n\t--------- --------- -------- -------- -------- -------- -------- -------- --------- --------\n\t\tChoose option:\n",
        "1. View all Residents",
        "2. Add Attendance",
        "3. Logout"
    ], [
        "\n\t\tMain Menu > Login > Admin > Add User > ",
        "\n\t--------- --------- -------- -------- -------- -------- -------- -------- --------- --------\n\t\tChoose option:\n",
        "1. Add Staff",
        "2. Add Resident",
        "3. Go Back"
    ], [
        "\n\t\tMain Menu > Login > Staff > Remove User > ",
        "\n\t--------- --------- -------- -------- -------- -------- -------- -------- --------- --------\n\t\tChoose option:\n",
        "1. Remove Staff",
        "2. Remove Resident",
        "3. Go Back"
    ]]
    if menu_name in menu_names:
        return menus[menu_names.index(menu_name)]


def store_user(category, user_name, password):
    if category == "staff":
        staff_names.append(user_name)
        staff_passwords.append(password)
    elif category == "resident":
        user_names.append(user_name)
        user_passwords.append(password)
        user_atts.append(0)


def add_resident_ui():
    validating = True
    while validating:
        name = input("Enter resident name: ")
        if not name.isalnum() and not name.isdigit():
            validating = False
        else:
            print("Invalid name entered.")
        password = input("Enter resident password: ")
    store_user("resident", name, password)
    


def add_staff_ui():
    validating = True
    while validating:
        name = input("Enter staff name: ")
        if not name.isalnum() and not name.isdigit():
            validating = False
        else:
            print("Invalid name entered.")
        password = input("Enter staff password: ")
    store_user("staff", name, password)


def remove_member(category, name):
    found = False
    if category == "resident":
        if name in user_names:
            idx = user_names.index(name)
            user_names.pop(idx)
            user_passwords.pop(idx)
            found = True
    elif category == "staff":
        if name in staff_names:
            idx = staff_names.index(name)
            staff_names.pop(idx)
            staff_passwords.pop(idx)
            found = True
    if found:
        print(name, "has been removed from", category)
    else:
        print("Couldn't find", name, "in", category)


def view_applications():
    for application in applications:
        print(application)
        print("---------------------------------------------------------------------------")


def remove_application():
    app_no = int(
        input("Enter application number you want to be removed: ")) - 1
    if app_no < len(applications):
        applications.pop(app_no)
    else:
        print("Cannot find the application")


def display_members(category, users, passwords):
    print(category + ":")
    print("------- -------- -------- -------- -------- -------- -------- ---------")
    print("Username\t|\tPassword", end='')
    if category == "Residents":
        print("\t|\tAttendance", end='')

    print("\n--------- -------- -------- -------- -------- -------- -------- ---------")

    for i in range(len(users)):
        print(users[i] , "\t\t|\t", passwords[i], end='')
        if category == "Residents":
            print("\t\t|\t", user_atts[i], end='')
    print("\n--------- -------- -------- -------- -------- -------- -------- ---------")


def add_notice_ui():
    notice = input("\nEnter Notice: ")
    store_notice(notice)


def store_notice(notice):
    notices.append(notice)


def show_notices():
    for notice in notices:
        print(notice)


def login(names, passwords, name, password):
    if name in names:  # find name
        idx = names.index(name)
        if passwords[idx] == password:  # check password
            return True
    return False


def add_attendance_ui():
    validating = False
    while validating:
        name = input("Enter user name: ")
        if name in user_names:
            idx = user_names.index(name)
            att = int(input("Enter attendance: "))
            if att > 0 and att < 90:
                validating = False
                store_attendance(att, idx)


def store_attendance(attendance, index):
    user_atts[index] = attendance


def make_application():
    applications.append(input(
        "Please enter your name\n and the password you want to use\nand the category you want to apply for\n(seperate them with \'_\'):\n\nInput: "))


def wait(optional_string):
    input(optional_string + "\nPress ENTER key to continue...")


def calculate_fees():
    global fees
    fees = []
    for att in user_atts:
        fees.append(att * 80)


def sort():
    global sorted_indexes
    global sorted_fees
    global sorted_names
    sorted_indexes = []
    copy_fees = fees.copy()
    sorted_fees = copy_fees.copy()
    sorted_fees.sort(reverse=True)
    for i in range(len(copy_fees)):
        idx = copy_fees.index(sorted_fees[i])
        sorted_names.append(user_names[idx])
        copy_fees.pop(idx)


def display_ordered_residents():
    calculate_fees()
    sort()
    print("\nResidents ordered w.r.t fees: ")
    print("--------- -------- -------- -------- -------- -------- ")
    print("Username\t|\tFees")
    print("--------- -------- -------- -------- -------- -------- ")

    for name, fee in zip(sorted_names, sorted_fees):
        print("\t\t", name, "\t\t|\t", fee)
    print("--------- -------- -------- -------- -------- -------- ")
    wait("")


def check_status():
    name = input("\nEnter your name: ")
    if name in user_names or name in staff_names:
        print("Your application has been accepted!")
    else:
        print("Your application has not been accepted yet...")


def load_demo_data():

    store_user("resident", "safee", "s123")
    store_user("resident", "adeel", "a123")
    store_user("resident", "hassan", "h123")
    store_user("resident", "javad", "j123")
    store_user("resident", "moeez", "m123")
    store_user("resident", "umair", "u123")
    store_user("resident", "mubshir", "m123")
    
    store_attendance(2, 0)
    store_attendance(34, 1)
    store_attendance(12, 2)
    store_attendance(4, 3)
    store_attendance(5, 4)
    store_attendance(20, 5)
    store_attendance(14, 6)

    store_user("staff", "adeel", "a123")
    store_user("staff", "bilal", "b123")
    store_user("staff", "nawaz", "n123")
    store_user("staff", "zardari", "z123")

    store_notice(
        "Welcome to the hostel. please read the notice carefully. It contains inportant information, which might be useful to you.")
    store_notice(
        "please read the notice carefully. Welcome to the hostel. It contains inportant information, which might be useful to you.")
    store_notice(
        "Welcome to the hostel. It contains inportant information, which might be useful to you. please read the notice carefully.")


main()
