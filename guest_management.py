import csv
import os

class Guest:
    guest_registry=[]
    dir_name = "data"
    file_name = "guests.csv"
    file_path = f"{dir_name}/{file_name}"

    def __init__(self, guest_id, full_name, phone_number, id_number, date_of_birth, save=True):
        self.guest_id = guest_id
        self.full_name = full_name
        self.phone_number = phone_number
        self.id_number = id_number
        self.date_of_birth = date_of_birth
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
                    "ID Number",
                    "Date of Birth"
                ])
            writer.writerow([
                self.guest_id,
                self.full_name,
                self.phone_number,
                self.id_number,
                self.date_of_birth
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
                "ID Number",
                "Date of Birth"
            ])

            for guest in cls.guest_registry:
                writer.writerow([
                    guest.guest_id,
                    guest.full_name,
                    guest.phone_number,
                    guest.id_number,
                    guest.date_of_birth
                ])

def load_guest_data():
    if not os.path.exists(Guest.file_path):
        return
    else:
        with open(Guest.file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                guest = Guest(
                    row["Guest ID"],
                    row["Full Name"],
                    row["Phone Number"],
                    row["ID Number"],
                    row["Date of Birth"],
                    save = False
                )
            #Guest.guest_registry.append(guest) #Appends all guests from csv to memory
    return
