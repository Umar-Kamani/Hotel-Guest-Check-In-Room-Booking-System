
### Guest class

from tabulate import tabulate


def create_new_guest():
    print("***********************************")
    print("Welcome to the Guest Creation Wizard")
    print("************************************")

    # Guest ID input
    while True:
        guest_id = input("Please enter the Guest ID: ") #This asks for a new guest id
        try:
            guest_id = str(guest_id)
            if not guest_id.strip():
                print("Guest ID cannot be empty. Please try again.")
                continue
        except ValueError:
            print("Invalid Guest ID format. Please enter  only digits.")
            continue

        if any(guest.guest_id == guest_id for guest in guest_class.guest):
            print("Guest ID is already taken. Please try again.")
        else:
            break

    print("___________________________________")
    # Guest Full name input
    while True:
        full_name = input("Please enter the guest's full name: ")
        if not full_name.strip():
            print("Full name cannot be empty. Please try again.")
        else:
            break

    print("___________________________________")
    # Phone number input
    while True:
        guest_phone_number = input("Please enter your phone number: ")
        try:
            if not guest_phone_number.isdigit() or len(guest_phone_number) != 10:  # this function checks for a valid 10 digit phone number
                print("Invalid phone number. Phone number must be 10 digits long.")
            else:
                break
        except ValueError:
            print("Phone number is invalid. Must be 10 digits long.")
    print("___________________________________")
    # Guest ID number input
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


    def __init__(self, guest_id, full_name, phone_number, id_number, date_of_birth):
        self.guest_id = guest_id
        self.full_name = full_name
        self.phone_number = phone_number
        self.id_number = id_number
        self.date_of_birth = date_of_birth
        self.validate()
