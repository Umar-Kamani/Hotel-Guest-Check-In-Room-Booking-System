import os
from datetime import datetime
from tabulate import tabulate


def create_new_guest():
    print("___________________________________")
    print("Welcome to the Guest Creation Wizard")
    print("___________________________________")

    # Guest ID input (check duplicates) #to auto-generate guestid
    while True:
        guest_id = input("Please enter the Guest ID: ")
        if not guest_id.strip():
            print("Guest ID cannot be empty. Please try again.")
            continue
        existing = Guest.load_from_file()
        if any(g.guest_id == guest_id for g in existing):
            print("Guest ID is already taken. Please try again.")
        else:
            break

    print("___________________________________")
    # Full name input
    while True: #validate inputs, since user can enter anything as name even numbers etc..
        full_name = input("Please enter the guest's full name: ")
        if not full_name.strip():
            print("Full name cannot be empty. Please try again.")
        else:
            break

    print("___________________________________")
    # Phone number input
    while True:
        phone_number = input("Please enter the guest's phone number: ")
        if not phone_number.strip():
            print("Phone number cannot be empty. Please try again.")
            continue
        if not any(ch.isdigit() for ch in phone_number):
            print("Phone number must contain digits. Please try again.")
        else:
            break

    print("___________________________________")
    # ID number input
    while True:
        id_number = input("Please enter the guest's ID/Passport number: ")
        if not id_number.strip():
            print("ID number cannot be empty. Please try again.")
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

    guest = Guest(guest_id, full_name, phone_number, id_number, date_of_birth)

    print("___________________________________________________________")
    print("Guest Successfully Created, please verify guest details below:\n")
    data = {
        "Guest ID": guest_id,
        "Full Name": full_name,
        "Phone Number": phone_number,
        "ID Number": id_number,
        "Date of Birth": date_of_birth,
    }
    if tabulate:
        print(tabulate([data], headers="keys", tablefmt="fancy_grid"))
    else:
        for k, v in data.items():
            print(f"{k}: {v}")
