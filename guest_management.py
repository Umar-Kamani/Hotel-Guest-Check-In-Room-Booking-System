import guest_class
from tabulate import tabulate


def create_new_guest() :
     print("___________________________________")
print("Welcome to the Guest Creation Wizard")
print("___________________________________")

# Guest ID input
from datetime import datetime

class Guest:
    guest_registry = []
    guest_id = 0

    def __init__(self, full_name, phone_number, id_number, date_of_birth):
        Guest.guest_id += 1
        self.guest_id = f"G{Guest.guest_id:03d}"
        self.full_name = full_name
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth

        Guest.guest_registry.append(self)

        print("___________________________________")
    # Full name input
while True:
        full_name = input("Please enter the guest's full name: ")
        if not full_name.strip():
            print("Full name cannot be empty. Please try again.")
        else:
            break
        if any(char.isdigit() for char in full_name):
            print("Full name cannot contain numbers. Please enter only letters.")
            continue

print("___________________________________")
    # Phone number input
while True:
        guest_phone_number = input("Please enter the guest's phone number: ")
        try:
            if not guest_phone_number.isdigit() or len(guest_phone_number) != 10:
                print("Invalid phone number. Contact  must be 10 digits long.")
            else:
                break
            except ValueError:
            print("Invalid phone number. Contact  must be 10 digits long.")

    print("___________________________________")

    print("___________________________________")
    # Date of birth input
    while True:
        date_of_birth = input("Please enter the Date of Birth (YYYY-MM-DD): ")
        try:
            datetime.strptime(date_of_birth, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    guest = guest_class.guest(guest_id, full_name, guest_phone_number, guest_id_number, date_of_birth)
    print("___________________________________________________________")
    print("Guest has Successfully been  added, please verify guest details below:\n")
    guest_data = {
        "Guest ID": guest_id,
        "Full Name": full_name,
        "Phone Number": guest_phone_number,
        "ID Number": guest_id_number,
        "Date of Birth": date_of_birth,
    }
    print(tabulate([[guest_data ], headers="keys", tablefmt="fancy_grid"))
