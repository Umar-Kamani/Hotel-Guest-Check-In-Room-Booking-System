import guest_class
from tabulate import tabulate
from datetime import datetime


def create_new_guest():
    print("___________________________________")
    print("Welcome to the Guest Creation Wizard")
    print("___________________________________")

    guest_id = guest_class.Guest.get_next_guest_id()

    # Passport number input
    while True:
        guest_passport_number = input("Please enter the guest Passport number: ").strip()
        if any(k.guest_passport_number == guest_passport_number for k in guest_class.Guest.guest_registry):
            print("Guest passport number is already taken. Please try again.")
        else:
            break
    print("___________________________________")

    # First name input
    while True:
        first_name = input("Please enter the guest's first name: ").strip().capitalize()
        if not first_name.isalpha():
            print("First name must contain only letters.")
        else:
            break

    # Last name input
    while True:
        last_name = input("Please enter the guest's last name: ").strip().capitalize()
        if not last_name.isalpha():
            print("Last name must contain only letters.")
        else:
            break

    guest_full_name = f"{first_name} {last_name}"
    print("___________________________________")

    # Phone number input
    while True:
        guest_phone_number = input("Please enter the guest's phone number: ").strip()
        if not guest_phone_number.isdigit() or len(guest_phone_number) < 10:
            print("Invalid phone number.")
        else:
            break
    print("___________________________________")

    # Date of Birth input
    while True:
        guest_date_of_birth = input("Please enter the Date of Birth (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(guest_date_of_birth, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format.")
    print("___________________________________")

    guest = guest_class.Guest( guest_id, guest_passport_number, guest_full_name, guest_phone_number, guest_date_of_birth, None, None)
    print("___________________________________________________________")
    print("Guest Successfully Created, please verify guest details below:\n")
    guest_data = {
        "Guest ID": guest_id,
        "Passport Number": guest_passport_number,
        "Full Name": guest_full_name,
        "Phone Number": guest_phone_number,
        "Date of Birth": guest_date_of_birth
    }
    print(tabulate(guest_data, headers="keys", tablefmt="fancy_grid"))


def modify_guest():
    print("___________________________________")
    print("Welcome to the Guest Modification Menu")
    print("___________________________________")

    # Select guest to modify
    while True:
        guest_passport_number_modify = input("Please enter the passport number of the guest you want to modify: ").strip()
        if any(k.passport_number == guest_passport_number_modify for k in guest_class.Guest.guest_registry):
            break
        else:
            print("Guest doesn't exist. Please enter a valid passport number.")

    # Fetch the guest details
    old_guest_filter = [k for k in guest_class.Guest.guest_registry if k.guest_passport_number == guest_passport_number_modify]
    old_guest_list = []
    for k in old_guest_filter:
        old_guest_list.append({
            "Passport Number": k.guest_passport_number,
            "Full Name": k.guest_full_name,
            "Phone Number": k.guest_phone_number,
            "Date of Birth": k.guest_date_of_birth
        })

    print("\nPlease verify guest details below:")
    print(tabulate(old_guest_list, headers="keys", tablefmt="fancy_grid"))

    print("\nGuest Details to Modify:")
    print("1. Passport Number")
    print("2. Full Name")
    print("3. Phone Number")
    print("4. Date of Birth")
    print("5. Exit")

    while True:
        details_modify = input("Please select guest detail to modify: ").strip()
        if details_modify not in ('1', '2', '3', '4', '5', 'exit'):
            print("Invalid choice. Please try again.")
        else:
            break

    # Call appropriate modification function
    if details_modify == '1':
        edit_guest_passport_number(guest_passport_number_modify)
    elif details_modify == '2':
        edit_guest_full_name(guest_passport_number_modify)
    elif details_modify == '3':
        edit_guest_phone_number(guest_passport_number_modify)
    elif details_modify == '4':
        edit_guest_date_of_birth(guest_passport_number_modify)
    else:
        return


def edit_guest_passport_number(guest_passport_number_modify):
    while True:
        new_guest_passport_number = input("Please enter the new guest passport number: ").strip()
        if any(k.guest_passport_number == new_guest_passport_number for k in guest_class.Guest.guest_registry):
            print("Guest Passport Number already exists. Please enter a new one.")
        else:
            break

    for k in guest_class.Guest.guest_registry:
        if k.guest_passport_number == guest_passport_number_modify:
            k.guest_passport_number = new_guest_passport_number
            guest_class.Guest.save_after_modification()
            print("Guest Passport Number Updated")
            view_guest_after_modification(new_guest_passport_number)


def edit_guest_full_name(guest_passport_number_modify):
    first = input("Enter new first name: ").capitalize()
    last = input("Enter new last name: ").capitalize()
    for k in guest_class.Guest.guest_registry:
        if k.guest_passport_number == guest_passport_number_modify:
            k.guest_full_name = f"{first} {last}"
            guest_class.Guest.save_after_modification()
            print("Guest Full Name Updated")
            view_guest_after_modification(guest_passport_number_modify)


def edit_guest_phone_number(guest_passport_number_modify):
    while True:
        new_guest_phone_number = input("Please enter the new guest phone number: ").strip()
        if not new_guest_phone_number.isdigit() or len(new_guest_phone_number) <= 10:
            print("Invalid phone number.")
        elif any(k.phone_number == new_guest_phone_number for k in guest_class.Guest.guest_registry):
            print("Phone number already exists. Please enter a new one.")
        else:
            break

    for k in guest_class.Guest.guest_registry:
        if k.guest_passport_number == guest_passport_number_modify:
            k.guest_phone_number = new_guest_phone_number
            guest_class.Guest.save_after_modification()
            print("Guest Phone Number Updated")
            view_guest_after_modification(guest_passport_number_modify)


def edit_guest_date_of_birth(guest_passport_number_modify):
    while True:
        new_guest_date_of_birth = input("Enter new DOB (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(new_guest_date_of_birth, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format.")

    for k in guest_class.Guest.guest_registry:
        if k.guest_passport_number == guest_passport_number_modify:
            k.date_of_birth = new_guest_date_of_birth
            guest_class.Guest.save_after_modification()
            print("Guest Date of Birth Updated")
            view_guest_after_modification(guest_passport_number_modify)


def view_guest_after_modification(guest_passport_number_modify):
    guest_view = []

    for k in guest_class.Guest.guest_registry:
        if k.passport_number.strip() == guest_passport_number_modify.strip():
            guest_view.append({
                "Passport Number": k.passport_number,
                "Full Name": k.full_name,
                "Phone Number": k.phone_number,
                "Date of Birth": k.date_of_birth
            })

    if not guest_view:
        print("No guest record found.")
        return

    print(tabulate(guest_view, headers="keys", tablefmt="fancy_grid"))


def main_menu():
    guest_class.load_guest_data()
    while True:
        print("\n1. Create new guest")
        print("2. View All Guests")
        print("3. View One Guest")
        print("4. Modify Guest")
        print("5. Delete Guest")
        print("6. Exit")
        choice = input("Choose: ").strip()

        if choice == '1':
            create_new_guest()
        elif choice == '4':
            modify_guest()
        elif choice == '6':
            break


if __name__ == "__main__":
    main_menu()
