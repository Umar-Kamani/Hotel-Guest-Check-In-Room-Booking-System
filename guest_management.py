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
        if any(guest.guest_passport_number == guest_passport_number for guest in guest_class.Guest.guest_registry):
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
    for n in guest_class.Guest.guest_registry:
        if n.guest_passport_number == guest_passport_number:
            new_guest_data.append({
                "Guest ID": guest.guest_id,
                "Full Name": guest_full_name,
                "Phone Number": guest_phone_number,
                "Date of Birth": guest_date_of_birth,
                "Passport Number": guest_passport_number
            })

    print(tabulate(new_guest_data, headers="keys", tablefmt="fancy_grid"))



def modify_room():
    print("___________________________________")
    print("Welcome to the Guest Modification Menu")
    print("___________________________________")

    while True:
        guest_passport_number_modify = input("Please enter the passport number of the Guest you want to modify: ")
        try:
            guest_passport_number_modify = int(guest_passport_number_modify)
            if any(guest.guest_passport_number == guest_passport_number_modify for guest in guest_class.Guest.guest_registry):
            else:
                print("Guest doesn't exist. Please enter a valid Guest Passsport number.")
        except ValueError:
            print("Invalid Guest Passport Number. Please try again.")

     old_guest_filter=[k for k in guest_class.Guest.guest_registry if k.guest_passport_number == guest_passport_number_modify]
    old_guest_list=[]
    for k in old_guest_filter:
        if k.geust_passport_number == guest_passport_number_modify:
            old_guest_list.append({
                "Passport Number": k.guest_passport_number,
        "Full Name": k.guest_full_name,
        "Phone Number": k.guest_phone_number,
        "Date of Birth": k.guest_date_of_birth
            })

    print("\nPlease verify room details below:")

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
