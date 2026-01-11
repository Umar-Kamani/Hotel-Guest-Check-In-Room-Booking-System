import guest_class
from tabulate import tabulate
from datetime import datetime

def create_new_guest():
    print("___________________________________")
    print("Welcome to the Guest Creation Wizard")
    print("___________________________________")

    # Generate Guest ID
    guest_id = len(guest_class.Guest.guest_registry) + 1 #change this similar to the budget tracker id

    # Guest Passport Number input
    while True:
        guest_passport_number = input("Please enter the guest's Passport number: ")
        if not guest_passport_number.strip():
            print("Passport number cannot be empty. Please try again.")
            continue
        else:
            break

    # Full name input
    while True:
        first_name = input("Please enter the guest's first name: ").capitalize()
        if not first_name.strip():
            print("Guest first name cannot be empty. Please try again.")
            continue
        if not first_name.isalpha():
            print("Guest first name must contain only letters. Please try again.")
        else:
            break
    while True:
        last_name = input("Please enter the guest's last name: ").capitalize()
        if not last_name.strip():
            print("Guest first name cannot be empty. Please try again.")
        if not last_name.isalpha():
            print("Guest first name must contain only letters. Please try again.")
        else:
            break

    full_name = first_name + " " + last_name

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

    guest = guest_class.Guest(guest_id, full_name, guest_phone_number, date_of_birth, guest_passport_number)

    print("___________________________________________________________")
    print("Guest has Successfully been added, please verify guest details below:\n")

    guest_data = [{
        "Guest ID": guest_id,
        "Guest Passport Number": guest_passport_number,
        "Full Name": full_name,
        "Phone Number": guest_phone_number,
        "Date of Birth": date_of_birth
    }]

    print(tabulate(guest_data, headers="keys", tablefmt="fancy_grid"))
    return


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
                "ID/Passport": k.id_number
            })

            print("\nPlease verify guest details below:")
            print(tabulate(old_guest_list, headers="keys", tablefmt="fancy_grid"))
            print("Guest Details")
            print("1.Guest Passport Number")
            print("2. Full Name")
            print("3. Phone Number")
            print("4. Date of Birth")
            print("5. Exit")
            while True:
                details_modify = input("Please select guest details to modify: ")
                if details_modify not in ('1', '2', '3', '4', '5', '6', 'exit'):
                    print("Invalid choice. Please try again.")
                else:
                    break
            # Menu system that calls the appropriate function
            if details_modify == '1':
                edit_guest_passport_number(guest_passport_number_modify)
            elif details_modify == '2':
                edit_full_name(guest_passport_number_modify)
            elif details_modify == '3':
                edit_phone_number(guest_passport_number_modify)
            elif details_modify == '4':
                edit_date_of_birth(guest_passport_number_modify)
            else:
                return

        def edit_guest_passport_number(guest_passport_number_modify):
            while True:
                new_guest_passport_number_id = input("Please enter the new guest Passport: ")
                try:
                    new_guest_passport_number = int(new_guest_passport_number)
                    if new_guest_passport_number == guest_passport_number_modify:
                        print("This is the same guest ID. No changes made.")
                        return
                    if any(guest.guest_id == new_guest_passport_number for guest in guest_class.Guest.guest_registry):
                        print("Guest ID already exists. Please enter a new guest ID.")
                        continue
                    else:
                        break
                except ValueError:
                    print("Invalid guest Passport Number. Please try again.")

            for k in guest_class.Guest.guest_registry:
                if k.guest_passport_number == guest_passport_number_modify:
                    k.guest_id = new_guest_passport_number
                    guest_class.Guest.save_after_modification()
                    print("Guest Passport Number Updated")
                    view_modified_guest(new_guest_passport_number)

def edit_full_name(guest_id_modify):
    while True:
        first_name = input("Please enter the guest's first name: ").strip().capitalize()
        if not first_name:
            print("Guest first name cannot be empty. Please try again.")
            continue
        if not first_name.replace(" ", "").replace("-", "").replace("'", "").isalpha():
            print("Guest first name must contain only letters. Please try again.")
            continue

        last_name = input("Please enter the guest's last name: ").strip().capitalize()
        if not last_name:
            print("Guest last name cannot be empty. Please try again.")
            continue
        if not last_name.replace(" ", "").replace("-", "").replace("'", "").isalpha():
            print("Guest last name must contain only letters. Please try again.")
            continue
        else:
            new_full_name = first_name + " " + last_name
            break

    for k in guest_class.Guest.guest_registry:
        if k.guest_id == guest_id_modify:
            k.full_name = new_full_name
            guest_class.Guest.save_after_modification()
            print("Full Name Updated")
    view_modified_guest(guest_id_modify)

def edit_phone_number(guest_id_modify):
    while True:
        new_phone_number = input("Please enter the new phone number: ")
        if not new_phone_number.isdigit():
            print("Invalid phone number. Please try again.")
            continue
        else:
            break

            for k in guest_class.Guest.guest_registry:
                if k.guest_id == guest_id_modify:
                    k.phone_number = new_phone_number
                    guest_class.Guest.save_after_modification()
                    print("Phone Number Updated")
            view_modified_guest(guest_id_modify)

def edit_date_of_birth(guest_id_modify):
    while True:
        new_date_of_birth = input("Please enter the new Date of Birth (YYYY-MM-DD): ")
        try:
            datetime.strptime(new_date_of_birth, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    for k in guest_class.Guest.guest_registry:
        if k.guest_id == guest_id_modify:
            k.date_of_birth = new_date_of_birth
            guest_class.Guest.save_after_modification()
            print("Date of Birth Updated")
    view_modified_guest(guest_id_modify)

        def view_modified_guest(modified_guest_id):
            view_guest = []
            for k in guest_class.Guest.guest_registry:
                if k.guest_id == modified_guest_id:
                    view_guest.append({
                        "Guest ID": k.guest_id,
                        "Full Name": k.full_name,
                        "Phone Number": k.phone_number,
                        "ID Number": k.id_number,
                        "Date of Birth": k.date_of_birth,
                    })
            print(tabulate(view_guest, headers="keys", tablefmt="fancy_grid"))

        def view_all_guests():
            all_guests = []
            for guest in guest_class.Guest.guest_registry:
                all_guests.append({
                    "Guest ID": guest.guest_id,
                    "Guest Passport Number": guest.guest_passport_number,
                    "Full Name": guest.full_name,
                    "Phone Number": guest.phone_number,
                    "ID Number": guest.id_number,
                    "Date of Birth": guest.date_of_birth,
                })
            print(tabulate(all_guests, headers="keys", tablefmt="fancy_grid"))

        def view_specific_guest():
            while True:
                view_guest_id = input("Please enter the guest ID of the guest you want to view: ")
                try:
                    view_guest_id = int(view_guest_id)
                    if any(guest.guest_id == view_guest_id for guest in guest_class.Guest.guest_registry):
                        break
                    else:
                        print("Guest doesn't exist. Please enter a valid guest ID.")
                except ValueError:
                    print("Invalid guest ID. Please try again.")
            specific_guest_list = []

            for guest in guest_class.Guest.guest_registry:
                if guest.guest_id == view_guest_id:
                    specific_guest_list.append({
                        "Guest ID": guest.guest_id,
                        "Guest Passport Number": guest.guest_passport_number,
                        "Full Name": guest.full_name,
                        "Phone Number": guest.phone_number,
                        "ID Number": guest.id_number,
                        "Date of Birth": guest.date_of_birth,
                    })
            print(f"Please find all details about guest {view_guest_id} below.")
            print(tabulate(specific_guest_list, headers="keys", tablefmt="fancy_grid"))

create_new_guest()
