import guest_class
from tabulate import tabulate
from datetime import datetime


def create_new_guest():
    print("___________________________________")
    print("Welcome to the Guest Creation Wizard")
    print("___________________________________")

    while True:
        guest_passport_number=input("Please enter the guest Passport number: ") 
        if any(guest.passport_number == guest_passport_number for guest in guest_class.Guest.guest_registry):
            print("Guest passport number is already taken. Please try again.")
        else:
            break
    print("___________________________________")


    while True:
        first_name = input("Please enter the guest's first name: ").strip().capitalize()
        if not first_name or not first_name.isalpha():
            print("Invalid First name, first name must contain only letters.")
            continue
        break

    while True:
        last_name = input("Please enter the guest's last name: ").strip().capitalize()
        if not last_name or not last_name.isalpha():
            print("Invalid First name, last name must contain only letters.")
            continue
        break

    guest_full_name = f"{first_name} {last_name}"
    print("___________________________________")

    while True:
        guest_phone_number = input("Please enter the guest's phone number: ").strip()
        if not guest_phone_number.isdigit():
            print("Invalid phone number.")
            continue
        break
    print("___________________________________")

    while True:
        guest_date_of_birth = input("Please enter the Date of Birth (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(guest_date_of_birth, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format.")

    guest = guest_class.Guest(
        guest_full_name,
        guest_phone_number,
        guest_date_of_birth,
        guest_passport_number
    )

    new_guest_data_filter=[n for n in guest_class.Guest.guest_registry]
    new_guest_data=[]
    for guest in new_guest_data_filter:
        if guest.passport_number == guest_passport_number:
            new_guest_data.append({
                "Guest ID": guest.id,
                "Full Name": guest_full_name,
                "Phone Number": guest_phone_number,
                "Date of Birth": guest_date_of_birth,
                "Passport Number": guest_passport_number
            })

    print(tabulate(new_guest_data, headers="keys", tablefmt="fancy_grid"))

def modify_guest():
    print("___________________________________")
    print("Welcome to the Guest Modification Menu")
    print("___________________________________")

    while True:
        guest_passport_number_modify = input("Please enter the passport number of the Guest you want to modify: ")
        try:
            if any(guest.passport_number == guest_passport_number_modify for guest in guest_class.Guest.guest_registry):
                break
            else:
                print("Guest doesn't exist. Please enter a valid Guest Passport number.")
        except ValueError:
            print("Invalid Guest Passport Number. Please try again.")

    old_guest_filter=[k for k in guest_class.Guest.guest_registry if k.passport_number == guest_passport_number_modify]
    old_guest_list=[]
    for k in old_guest_filter:
        old_guest_list.append({
        "Full Name": k.full_name,
        "Phone Number": k.phone_number,
        "Date of Birth": k.date_of_birth,
        "Passport Number": k.passport_number
        })

    print("\nPlease verify guest details below:")
    print(tabulate(old_guest_list, headers="keys", tablefmt="fancy_grid"))

    print("Guest Details")
    print("1. Full Name")
    print("2. Phone Number")
    print("3. Date of Birth")
    print("4. Passport/ID Number")
    print("5. Exit")

    while True:
        guest_modify_choice = input("Please select guest detail to modify: ").lower() #prompts the user to choose the detail of the guest to modify
        if guest_modify_choice not in ('1', '2', '3', '4', '5', 'exit'): #simple statement to validate input
            print("Invalid choice. Please try again.")
        else:
            break

    if guest_modify_choice == "1":
        edit_guest_full_name(guest_passport_number_modify)
    elif guest_modify_choice == "2":
        edit_guest_phone_number(guest_passport_number_modify)
    elif guest_modify_choice == "3":
        edit_guest_date_of_birth(guest_passport_number_modify)
    elif guest_modify_choice == "4":
        edit_guest_passport_number(guest_passport_number_modify)
    else:
        print("Returning to Main Menu.")

def edit_guest_passport_number(guest_passport_number_modify):
    while True:
        new_passport = input("Please enter the new passport number: ").strip()
        if not new_passport:
            print("Invalid Passport Number. Please try again.")
        if any(guest.passport_number == new_passport for guest in guest_class.Guest.guest_registry):
            print("Passport Number already exists. Please enter a different Passport Number.")
        else:
            break

    for g in guest_class.Guest.guest_registry:
        if g.passport_number == guest_passport_number_modify:
            g.passport_number = new_passport
            guest_class.Guest.save_after_modification()
            print("Passport Number has been updated.")
            view_modified_guest(new_passport)


def edit_guest_full_name(guest_passport_number_modify):
    while True:
        new_first_name = input("Enter new first name: ").capitalize().strip()
        if not new_first_name:
            print("Invalid First Name. Please try again.")
        else:
            break
    while True:
        new_last_name = input("Enter new last name: ").capitalize().strip()
        if not new_last_name:
            print("Invalid Last Name. Please try again.")
        else:
            break
    new_full_name = f"{new_first_name} {new_last_name}"
    print("New Full Name: ", new_full_name)

    for g in guest_class.Guest.guest_registry:
        if g.passport_number == guest_passport_number_modify:
            g.full_name = new_full_name
            guest_class.Guest.save_after_modification()
            print("Full Name has been updated Successfully.")
            view_modified_guest(guest_passport_number_modify)

def edit_guest_phone_number(guest_passport_number_modify):
    while True:
        new_phone_number = input("Enter new phone number: ")
        if not new_phone_number.isdigit():
            print("Invalid Phone Number. Please try again.")
        else:
            break
    print("New Phone Number: ", new_phone_number)

    for g in guest_class.Guest.guest_registry:
        if g.passport_number == guest_passport_number_modify:
            g.phone_number = new_phone_number
            guest_class.Guest.save_after_modification()
            print("Phone Number has been updated Successfully.")
            view_modified_guest(guest_passport_number_modify)


def edit_guest_date_of_birth(guest_passport_number_modify):
    while True:
        new_date_of_birth = input("Enter new date of birth (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(new_date_of_birth, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format.")
    print("New Date of Birth: ", new_date_of_birth)

    for g in guest_class.Guest.guest_registry:
        if g.passport_number == guest_passport_number_modify:
            g.date_of_birth = new_date_of_birth
            guest_class.Guest.save_after_modification()
            print("Date of Birth has been updated Successfully.")
            view_modified_guest(guest_passport_number_modify)

def view_modified_guest(guest_passport_number_modify):
    modified_guest_list=[]
    for g in guest_class.Guest.guest_registry:
       if g.passport_number == guest_passport_number_modify:
           modified_guest_list.append({
               "Guest ID": g.id,
               "Guest Full Name": g.full_name,
               "Guest Phone Number": g.phone_number,
               "Date of Birth": g.date_of_birth,
               "Guest Passport Number": g.passport_number,
           })
    print(tabulate(modified_guest_list, headers="keys", tablefmt="fancy_grid"))

def view_all_guests():
    all_guest_list=[]
    for guest in guest_class.Guest.guest_registry:
        all_guest_list.append({
            "Guest ID": guest.id,
            "Guest Full Name": guest.full_name,
            "Guest Phone Number": guest.phone_number,
            "Date of Birth": guest.date_of_birth,
            "Guest Passport Number": guest.passport_number,
        })
    print(tabulate(all_guest_list, headers="keys", tablefmt="fancy_grid"))

guest_class.load_guest_data()
view_all_guests()
#create_new_guest()
modify_guest()