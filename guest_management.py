import guest_class
from tabulate import tabulate
from datetime import datetime


def create_new_guest():
    print("___________________________________")
    print("Welcome to the Guest Creation Wizard")
    print("___________________________________")

    # Generate Guest ID
    guest_id = len(guest_class.Guest.guest_registry) + 1

    # Full name input
    while True:
        first_name = input("Please enter the guest's first name: ").capitalize()
        if not first_name.strip():
            print("Guest first name cannot be empty. Please try again.")
        if not first_name.isalpha():
            print("Guest first name must contain only letters. Please try again.")
        last_name = input("Please enter the guest's last name: ").capitalize()
        if not last_name.strip():
            print("Guest first name cannot be empty. Please try again.")
        if not last_name.isalpha():
            print("Guest first name must contain only letters. Please try again.")
        else:
            full_name = first_name + " " + last_name
            break

    print("___________________________________")

    # Phone number input
    while True:
        guest_phone_number = input("Please enter the guest's phone number: ")
        if not guest_phone_number.isdigit():
            print("Invalid phone number. Please try again.")
        else:
            break

    print("___________________________________")

    # Date of birth input
    while True:
        date_of_birth = input("Please enter the Date of Birth (YYYY-MM-DD): ")
        try:
            datetime.strptime(date_of_birth, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    guest = guest_class.Guest(
        guest_id,
        full_name,
        guest_phone_number,
        date_of_birth
    )

    print("___________________________________________________________")
    print("Guest has Successfully been added, please verify guest details below:\n")

    guest_data = {
        "Guest ID": guest_id,
        "Full Name": full_name,
        "Phone Number": guest_phone_number,
        "Date of Birth": date_of_birth,
    }

    print(tabulate([guest_data], headers="keys", tablefmt="fancy_grid"))


def modify_guest():
    print("___________________________________")
    print("Welcome to the Guest Modification Menu")
    print("___________________________________")
    while True:
        guest_id_modify = input("Please enter the guest ID of the guest you want to amend: ")
        try:
            guest_id_modify = int(guest_id_modify)
            if any(guest.guest_id == guest_id_modify for guest in guest_class.Guest.guest_registry):
                break
            else:
                print("Guest doesn't exist. Please enter a valid guest ID.")
        except ValueError:
            print("Invalid guest ID. Please try again.")

    old_guest_filter = [k for k in guest_class.Guest.guest_registry if k.guest_id == guest_id_modify]
    old_guest_list = []

    for k in old_guest_filter:
        if k.guest_id == guest_id_modify:
            old_guest_list.append({
                "Guest ID": k.guest_id,
                "Full Name": k.full_name,
                "Phone Number": k.phone_number,
                "ID Number": k.id_number,
