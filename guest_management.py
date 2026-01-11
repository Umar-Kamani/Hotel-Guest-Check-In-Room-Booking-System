import guest_class
from tabulate import tabulate
from datetime import datetime


def create_new_guest():
    print("___________________________________")
    print("Guest Creation")
    print("___________________________________")

    guest_id = guest_class.Guest.get_next_guest_id()

    while True:
        passport_number = input("Please enter the guest's passport number: ").strip()
        if not passport_number:
            print("Passport number cannot be empty.")
            continue
        if guest_class.Guest.find_by_passport(passport_number):
            print("Passport number already exists.")
            continue
        break

    while True:
        first_name = input("Please enter the guest's first name: ").strip().capitalize()
        if not first_name:
            print("First name cannot be empty.")
            continue
        if not first_name.isalpha():
            print("First name must contain only letters.")
            continue
        break

    while True:
        last_name = input("Please enter the guest's last name: ").strip().capitalize()
        if not last_name:
            print("Last name cannot be empty.")
            continue
        if not last_name.isalpha():
            print("Last name must contain only letters.")
            continue
        break

    full_name = f"{first_name} {last_name}"

    while True:
        phone_number = input("Please enter the guest's phone number: ").strip()
        if not phone_number.isdigit() or len(phone_number) <= 10:
            print("Invalid phone number. Must contain only digits (min 10).")
            continue
        break

    while True:
        date_of_birth = input("Please enter the Date of Birth (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date_of_birth, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    guest = guest_class.Guest(guest_id, full_name, phone_number, date_of_birth, passport_number)

    print("\nGuest successfully added:\n")
    guest_data = [{
        "Guest ID": guest.guest_id,
        "Passport Number": guest.passport_number,
        "Full Name": guest.full_name,
        "Phone Number": guest.phone_number,
        "Date of Birth": guest.date_of_birth
    }]

    print(tabulate(guest_data, headers="keys", tablefmt="fancy_grid"))
    print("\nGuest added successfully!")


def modify_guest():
    print("___________________________________")
    print("Guest Modification")
    print("___________________________________")

    if not guest_class.Guest.guest_registry:
        print("No guests to modify.")
        return

    while True:
        passport_number = input("Please enter the passport number of the guest to amend: ").strip()
        guest = guest_class.Guest.find_by_passport(passport_number)
        if guest:
            break
        print("Guest not found. Please enter a valid passport number.")

    print("\nCurrent guest details:")
    guest_data = [{
        "Guest ID": guest.guest_id,
        "Passport Number": guest.passport_number,
        "Full Name": guest.full_name,
        "Phone Number": guest.phone_number,
        "Date of Birth": guest.date_of_birth
    }]
    print(tabulate(guest_data, headers="keys", tablefmt="fancy_grid"))

    while True:
        print("\nSelect field to modify:")
        print("1. Passport Number")
        print("2. Full Name")
        print("3. Phone Number")
        print("4. Date of Birth")
        print("5. Cancel")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            edit_passport_number(guest)
            break
        elif choice == '2':
            edit_full_name(guest)
            break
        elif choice == '3':
            edit_phone_number(guest)
            break
        elif choice == '4':
            edit_date_of_birth(guest)
            break
        elif choice == '5':
            print("Modification cancelled.")
            return
        else:
            print("Invalid choice. Please try again.")


def edit_passport_number(guest):
    while True:
        new_passport = input("Enter new passport number: ").strip()
        if not new_passport:
            print("Passport number cannot be empty.")
            continue
        if new_passport == guest.passport_number:
            print("This is the same passport number.")
            return
        if guest_class.Guest.find_by_passport(new_passport):
            print("Passport number already exists.")
            continue
        break

    old_passport = guest.passport_number
    guest.passport_number = new_passport
    guest_class.Guest.save_after_modification()
    print(f"Passport number updated from {old_passport} to {new_passport}")


def edit_full_name(guest):
    while True:
        first_name = input("Enter new first name: ").strip().capitalize()
        if not first_name:
            print("First name cannot be empty.")
            continue
        if not first_name.replace(" ", "").replace("-", "").isalpha():
            print("First name must contain only letters.")
            continue
        break

    while True:
        last_name = input("Enter new last name: ").strip().capitalize()
        if not last_name:
            print("Last name cannot be empty.")
            continue
        if not last_name.replace(" ", "").replace("-", "").isalpha():
            print("Last name must contain only letters.")
            continue
        break

    new_full_name = f"{first_name} {last_name}"
    old_name = guest.full_name
    guest.full_name = new_full_name
    guest_class.Guest.save_after_modification()
    print(f"Full name updated from '{old_name}' to '{new_full_name}'")


def edit_phone_number(guest):
    while True:
        new_phone = input("Enter new phone number: ").strip()
        if not new_phone.isdigit() or len(new_phone) < 8:
            print("Invalid phone number. Must contain only digits (min 8).")
            continue
        break

    old_phone = guest.phone_number
    guest.phone_number = new_phone
    guest_class.Guest.save_after_modification()
    print(f"Phone number updated from {old_phone} to {new_phone}")


def edit_date_of_birth(guest):
    while True:
        new_dob = input("Enter new Date of Birth (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(new_dob, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    old_dob = guest.date_of_birth
    guest.date_of_birth = new_dob
    guest_class.Guest.save_after_modification()
    print(f"Date of Birth updated from {old_dob} to {new_dob}")


def delete_guest():
    print("___________________________________")
    print("Guest Deletion")
    print("___________________________________")

    if not guest_class.Guest.guest_registry:
        print("No guests to delete.")
        return

    while True:
        passport_number = input("Enter passport number of guest to delete: ").strip()
        guest = guest_class.Guest.find_by_passport(passport_number)
        if guest:
            print(f"\nFound guest: {guest.full_name} (Passport: {guest.passport_number})")
            confirm = input("Are you sure you want to delete this guest? (yes/no): ").strip().lower()
            if confirm == 'yes':
                if guest_class.Guest.delete_by_passport(passport_number):
                    print(f"Guest with passport {passport_number} deleted successfully.")
                else:
                    print("Failed to delete guest.")
            else:
                print("Deletion cancelled.")
            break
        print("Guest not found. Please try again.")


def view_all_guests():
    if not guest_class.Guest.guest_registry:
        print("No guests in the system.")
        return

    all_guests = []
    for guest in guest_class.Guest.guest_registry:
        all_guests.append({
            "Guest ID": guest.guest_id,
            "Passport Number": guest.passport_number,
            "Full Name": guest.full_name,
            "Phone Number": guest.phone_number,
            "Date of Birth": guest.date_of_birth
        })

    print("\nAll Guests:")
    print(tabulate(all_guests, headers="keys", tablefmt="fancy_grid"))
    print(f"\nTotal guests: {len(all_guests)}")


def view_specific_guest():
    if not guest_class.Guest.guest_registry:
        print("No guests in the system.")
        return

    while True:
        passport_number = input("Enter passport number of guest to view: ").strip()
        guest = guest_class.Guest.find_by_passport(passport_number)
        if guest:
            guest_data = [{
                "Guest ID": guest.guest_id,
                "Passport Number": guest.passport_number,
                "Full Name": guest.full_name,
                "Phone Number": guest.phone_number,
                "Date of Birth": guest.date_of_birth
            }]
            print(f"\nGuest details for passport {passport_number}:")
            print(tabulate(guest_data, headers="keys", tablefmt="fancy_grid"))
            break
        print("Guest not found. Please try again.")


def main_menu():
    guest_class.load_guest_data()

    while True:
        try:
            print("\n" + "=" * 50)
            print("GUEST MANAGEMENT SYSTEM")
            print("=" * 50)
            print("1. Create New Guest")
            print("2. View All Guests")
            print("3. View Specific Guest")
            print("4. Modify Guest")
            print("5. Delete Guest")
            print("6. Exit")
            print("-" * 50)

            choice = input("Enter your choice (1-6): ").strip()

            if choice == '1':
                create_new_guest()
            elif choice == '2':
                view_all_guests()
            elif choice == '3':
                view_specific_guest()
            elif choice == '4':
                modify_guest()
            elif choice == '5':
                delete_guest()
            elif choice == '6':
                print("Exiting system. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main_menu()