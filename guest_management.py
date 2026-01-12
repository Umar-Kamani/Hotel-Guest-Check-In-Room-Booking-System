import guest_class
from tabulate import tabulate
from datetime import datetime


def create_new_guest():
    print("___________________________________")
    print("Welcome to the Guest Creation Wizard")
    print("___________________________________")

    guest_id = guest_class.Guest.get_next_guest_id()

    while True:
        guest_passport_number=input("Please enter the guest Passport number: ") 
        if any(guest.guest_passport_number == guest_passport_number for guest in guest_class.guest.guest_registry):
            print("Guest passport  number is already taken. Please try again.")
        else:
            break
    print("___________________________________")


    while True:
        first_name = input("Please enter the guest's first name: ").strip().capitalize()
        if not first_name or not first_name.isalpha():
            print("First name must contain only letters.")
            continue
        break

    while True:
        last_name = input("Please enter the guest's last name: ").strip().capitalize()
        if not last_name or not last_name.isalpha():
            print("Last name must contain only letters.")
            continue
        break
    guest_full_name = f"{first_name} {last_name}"
    print("___________________________________")

    while True:
        guest_phone_number = input("Please enter the guest's phone number: ").strip()
        if not guest_phone_number.isdigit() or len(guest_phone_number) <= 10:
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

    print("___________________________________")

    guest = guest_class.Guest(guest_id, guest_passport_number, guest_full_name, guest_phone_number, guest_date_of_birth)
    print("___________________________________________________________")
    print("Guest Successfully Created, please verify guest details below:\n")
    guest_data = {
        "Guest ID": guest.guest_id,
        "Passport Number": guest_passport_number,
        "Full Name": guest_full_name,
        "Phone Number": guest_phone_number,
        "Date of Birth": guest_date_of_birth
    }

    print(tabulate(guest_data, headers="keys", tablefmt="fancy_grid"))


def modify_guest():
    print("___________________________________")
    print("Guest Modification")
    print("___________________________________")

    while True:
        passport_number = input("Enter passport number: ").strip()
        guest = guest_class.Guest.find_by_passport(passport_number)
        if guest:
            break
        print("Guest not found.")

    guest_data = [{
        "Guest ID": guest.guest_id,
        "Passport Number": guest.guest_passport_number,
        "Full Name": guest.guest_full_name,
        "Phone Number": guest.guest_phone_number,
        "Date of Birth": guest.guest_date_of_birth
    }]
    print(tabulate(guest_data, headers="keys", tablefmt="fancy_grid"))

    print("1. Guest Passport Number")
    print("2. Guest Full Name")
    print("3. Guest Phone Number")
    print("4. Guest Date of Birth")

    while True:
        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            edit_guest_passport_number(guest)
            break
        elif choice == '2':
            edit_guest_full_name(guest)
            break
        elif choice == '3':
            edit_guest_phone_number(guest)
            break
        elif choice == '4':
            edit_guest_date_of_birth(guest)
            break
        else:
            print("Invalid choice.")


def edit_guest_passport_number(guest):
    new_passport = input("Enter new passport number: ").strip()
    guest.guest_passport_number = new_passport
    guest_class.Guest.save_after_modification()


def edit_guest_full_name(guest):
    first = input("Enter new first name: ").capitalize()
    last = input("Enter new last name: ").capitalize()
    guest.guest_full_name = f"{first} {last}"
    guest_class.Guest.save_after_modification()


def edit_guest_phone_number(guest):
    guest.guest_phone_number = input("Enter new phone number: ")
    guest_class.Guest.save_after_modification()
    view_modified_guest(guest.guest_passport_number)


def edit_guest_date_of_birth(guest):
    guest.guest_date_of_birth = input("Enter new DOB (YYYY-MM-DD): ")
    guest_class.Guest.save_after_modification()


def view_modified_guest(passport_number):
    guest = guest_class.Guest.find_by_passport(passport_number)
    if guest:
        print(tabulate([{
            "Guest ID": guest.guest_id,
            "Passport Number": guest.guest_passport_number,
            "Full Name": guest.guest_full_name,
            "Phone Number": guest.guest_phone_number,
            "Date of Birth": guest.guest_date_of_birth
        }], headers="keys", tablefmt="fancy_grid"))


def main_menu():
    guest_class.load_guest_data()
    while True:
        print("\n1.Create new guest 2.View All Guests 3.View one guest 4.Modify guests 5.Delete guests 6.Exit")
        choice = input("Choose: ")
        if choice == '1':
            create_new_guest()
        elif choice == '4':
            modify_guest()
        elif choice == '6':
            break


if __name__ == "__main__":
    main_menu()


if __name__ == "__main__":
    main_menu()
