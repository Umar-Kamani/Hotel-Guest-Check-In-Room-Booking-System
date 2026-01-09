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
        last_name = input("Please enter the guest's last name: ").capitalize()
        full_name = first_name+" "+last_name
        if not full_name.strip():
            print("Guest name cannot be empty. Please try again.")
        elif any(char.isdigit() for char in full_name):
            print("Guest name cannot contain numbers. Please enter only letters.")
        else:
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


create_new_guest()