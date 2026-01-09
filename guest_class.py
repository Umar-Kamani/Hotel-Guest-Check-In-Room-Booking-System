import csv
import os

class Guest:
    guest_registry=[]
    dir_name = "data"
    file_name = "guests.csv"
    file_path = f"{dir_name}/{file_name}"

    def __init__(self, guest_id, full_name, phone_number, date_of_birth, id_passport, save=True):
        self.guest_id = guest_id
        self.full_name = full_name
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.id_passport = id_passport

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
                    "ID/Passport",
                ])
            writer.writerow([
                self.guest_id,
                self.full_name,
                self.phone_number,
                self.date_of_birth,
                self.id_passport,
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
                "ID/Passport",
            ])

            for guest in cls.guest_registry:
                writer.writerow([
                    guest.guest_id,
                    guest.full_name,
                    guest.phone_number,
                    guest.date_of_birth,
                    guest.id_passport,
                ])

def load_guest_data():
    if not os.path.exists(Guest.file_path):
        return
    else:
        with open(Guest.file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                guest = Guest(
                    int(row["Guest ID"]),
                    row["Full Name"],
                    row["Phone Number"],
                    row["Date of Birth"],
                    row["ID/Passport"],
                    save = False
                )