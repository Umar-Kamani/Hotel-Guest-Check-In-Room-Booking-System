import csv
import os
 
class Guest:
    guest_registry = []
    dir_name = "data"
    file_name = "guests.csv"
    file_path = f"{dir_name}/{file_name}"
    guest_id = 0
 
    def __init__(self, full_name, phone_number, date_of_birth, passport_number, save=True):
        Guest.guest_id += 1
        self.id = Guest.guest_id
        self.full_name = full_name
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.passport_number = passport_number
 
        Guest.guest_registry.append(self)
        if save:
            self.save_to_csv()
 
    def save_to_csv(self):
        os.makedirs("data", exist_ok=True)
        guest_file_exists = os.path.exists(Guest.file_path)
        with open(Guest.file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if not guest_file_exists:
                writer.writerow([
                    "Guest ID",
                    "Full Name",
                    "Phone Number",
                    "Date of Birth",
                    "Passport Number",
                ])
            writer.writerow([
                self.id,
                self.full_name,
                self.phone_number,
                self.date_of_birth,
                self.passport_number,
            ])
 
    @classmethod
    def save_after_modification(cls):
        os.makedirs(cls.dir_name, exist_ok=True)
 
        with open(cls.file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                "Guest ID",
                "Full Name",
                "Phone Number",
                "Date of Birth",
                "Passport Number",
            ])
 
            for guest in cls.guest_registry:
                writer.writerow([
                    guest.id,
                    guest.full_name,
                    guest.phone_number,
                    guest.date_of_birth,
                    guest.passport_number,
                ])

    @classmethod
    def get_next_guest_id(cls):
        if cls.guest_registry:
            return max(guest.guest_id for guest in cls.guest_registry) + 1
        return 1
 
    @classmethod
    def find_by_passport(cls, passport_number):
        for guest in cls.guest_registry:
            if guest.passport_number == passport_number:
                return guest
        return None
 
    @classmethod
    def delete_by_passport(cls, passport_number):
        guest = cls.find_by_passport(passport_number)
        if guest:
            cls.guest_registry.remove(guest)
            cls.save_after_modification()
            return True
        return False
 
def load_guest_data():
    if not os.path.exists(Guest.file_path):
        return
 
    with open(Guest.file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Guest(
                row["Full Name"],
                row["Phone Number"],
                row["Date of Birth"],
                row["Passport Number"],
                save=False
            )
            guest_id = int(row["Booking ID"])
            Guest.guest_id = max(guest_id, Guest.guest_id) #compares booking from line 6 and the one we loaded from the csv file into memory and re-assigns it to the largest number