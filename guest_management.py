import guest_class
from tabulate import tabulate
from datetime import datetime
import sys


def create_new_guest():
    print("___________________________________")
    print("Welcome to the Guest Creation Wizard")
    print("___________________________________")

    guest_id = len(guest_class.Guest.guest_registry) + 1

    while True:
        guest_passport_number = input("Please enter the guest's Passport number: ").strip()
        if not guest_passport_number:
            print("Passport number cannot be empty. Please try again.")
            continue
        if any(g.guest_passport_number == guest_passport_number for g in guest_class.Guest.guest_registry):
            print("This passport number already exists. Please enter a unique one.")
            continue
        break

    while True:
        first_name = input("Please enter the guest's first name: ").strip().capitalize()
        if not first_name or not first_name.isalpha():
            print("Guest first name must be non-empty and letters only. Try again.")
            continue
        last_name = input("Please enter the guest's last name: ").strip().capitalize()
        if not last_name or not last_name.isalpha():
            print("Guest last name must be non-empty and letters only. Try again.")
            continue
        full_name = first_name + " " + last_name
        break

    while True:
        guest_phone_number = input("Please enter the guest's phone number: ").strip()
        if not guest_phone_number.isdigit():
            print("Invalid phone number. Please try again.")
            continue
        break

    while True:
        date_of_birth = input("Please enter the Date of Birth (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date_of_birth, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    guest_class.Guest(
        guest_id,
        guest_passport_number,
        full_name,
        guest_phone_number,
        date_of_birth
    )

    guest_data = [{
        "Guest ID": guest_id,
        "Guest Passport Number": guest_passport_number,
        "Full Name": full_name,
        "Phone Number": guest_phone_number,
        "Date of Birth": date_of_birth,
    }]
    print(tabulate(guest_data, headers="keys", tablefmt="fancy_grid"))
    print(f"\nGuest '{full_name}' with Passport Number '{guest_passport_number}' successfully added!\n")


def modify_guest():
    print("___________________________________")
    print("Welcome to the Guest Modification Menu")
    print("___________________________________")

    while True:
        passport_number = input("Enter Passport Number of the guest to modify: ").strip()
        guest = next((g for g in guest_class.Guest.guest_registry if g.guest_passport_number == passport_number), None)
        if guest:
            break
        print("Guest not found. Try again.")

    guest_data = [{
        "Guest Passport Number": guest.guest_passport_number,
        "Full Name": guest.full_name,
        "Phone Number": guest.phone_number,
        "Date of Birth": guest.date_of_birth,
    }]
    print("\nPlease verify guest details below:")
    print(tabulate(guest_data, headers="keys", tablefmt="fancy_grid"))

    print("Guest Details")
    print("1. Guest Passport Number")
    print("2. Full Name")
    print("3. Phone Number")
    print("4. Date of Birth")
    print("5. Exit")

    while True:
        details_modify = input("Select detail to modify: ").strip()
        if details_modify in ('1','2','3','4','5'):
            break
        print("Invalid choice. Try again.")

    if details_modify == '1':
        edit_guest_passport_number(passport_number)
    elif details_modify == '2':
        edit_full_name(passport_number)
    elif details_modify == '3':
        edit_phone_number(passport_number)
    elif details_modify == '4':
        edit_date_of_birth(passport_number)
    else:
        return


def edit_guest_passport_number(old_passport_number):
    while True:
        new_passport_number = input("Enter new Passport Number: ").strip()
        if new_passport_number == old_passport_number:
            print("This is the same passport number. No changes made.")
            return
        if any(g.guest_passport_number == new_passport_number for g in guest_class.Guest.guest_registry):
            print("This passport number already exists. Try again.")
            continue
        break

    for guest in guest_class.Guest.guest_registry:
        if guest.guest_passport_number == old_passport_number:
            guest.guest_passport_number = new_passport_number
            guest_class.Guest.save_after_modification()
            print("Passport Number Updated")
            break

    view_modified_guest(new_passport_number)


def edit_full_name(passport_number):
    while True:
        first_name = input("Enter first name: ").strip().capitalize()
        if not first_name.isalpha():
            print("Invalid first name. Try again.")
            continue
        last_name = input("Enter last name: ").strip().capitalize()
        if not last_name.isalpha():
            print("Invalid last name. Try again.")
            continue
        new_full_name = first_name + " " + last_name
        break

    for guest in guest_class.Guest.guest_registry:
        if guest.guest_passport_number == passport_number:
            guest.full_name = new_full_name
            guest_class.Guest.save_after_modification()
            print(f"Full Name Updated to '{new_full_name}'")
            break

    view_modified_guest(passport_number)


def edit_phone_number(passport_number):
    while True:
        new_phone_number = input("Enter new phone number: ").strip()
        if not new_phone_number.isdigit():
            print("Invalid phone number. Try again.")
            continue
        break

    for guest in guest_class.Guest.guest_registry:
        if guest.guest_passport_number == passport_number:
            guest.phone_number = new_phone_number
            guest_class.Guest.save_after_modification()
            print(f"Phone Number Updated to '{new_phone_number}'")
            break

    view_modified_guest(passport_number)


def edit_date_of_birth(passport_number):
    while True:
        new_dob = input("Enter new Date of Birth (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(new_dob, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Try again.")

    for guest in guest_class.Guest.guest_registry:
        if guest.guest_passport_number == passport_number:
            guest.date_of_birth = new_dob
            guest_class.Guest.save_after_modification()
            print(f"Date of Birth Updated to '{new_dob}'")
            break

    view_modified_guest(passport_number)


def view_modified_guest(passport_number):
    guest_data = [g.__dict__ for g in guest_class.Guest.guest_registry if g.guest_passport_number == passport_number]
    if guest_data:
        guest_data = [{
            "Guest Passport Number": guest_data[0]["guest_passport_number"],
            "Full Name": guest_data[0]["full_name"],
            "Phone Number": guest_data[0]["phone_number"],
            "Date of Birth": guest_data[0]["date_of_birth"],
        }]
        print(tabulate(guest_data, headers="keys", tablefmt="fancy_grid"))


def view_all_guests():
    guest_data = [{
        "Guest Passport Number": g.guest_passport_number,
        "Full Name": g.full_name,
        "Phone Number": g.phone_number,
        "Date of Birth": g.date_of_birth,
    } for g in guest_class.Guest.guest_registry]
    print(tabulate(guest_data, headers="keys", tablefmt="fancy_grid"))


def view_specific_guest():
    while True:
        passport_number = input("Enter Passport Number of guest to view: ").strip()
        guest = next((g for g in guest_class.Guest.guest_registry if g.guest_passport_number == passport_number), None)
        if guest:
            break
        print("Guest not found. Try again.")

    guest_data = [{
        "Guest Passport Number": guest.guest_passport_number,
        "Full Name": guest.full_name,
        "Phone Number": guest.phone_number,
        "Date of Birth": guest.date_of_birth,
    }]
    print(tabulate(guest_data, headers="keys", tablefmt="fancy_grid"))

def main_menu():
    try:
        while True:
            print("\n========== Guest Management System ==========")
            print("1. Create New Guest")
            print("2. Modify Guest")
            print("3. View All Guests")
            print("4. View Specific Guest")
            print("5. Exit")
            choice = input("Please choose an option: ").strip()

            if choice == '1':
                create_new_guest()
            elif choice == '2':
                modify_guest()
            elif choice == '3':
                view_all_guests()
            elif choice == '4':
                view_specific_guest()
            elif choice == '5':
                delete_guest()
            elif choice == '6':
                print("Exiting Guest Management System.")
                break
            else:
                print("Invalid option. Try again.")
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Exiting gracefully...")
        sys.exit(0)


if __name__ == "__main__":
    main_menu()