import os
import csv
import secrets
import string

def random_booking_id(): #generates a random booking ID
    length = 6
    random_string = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))
    return random_string

class Booking:
    booking_registry = []
    dir_name = "data"
    file_name = "bookings.csv"
    file_path = f"{dir_name}/{file_name}"
    booking_id = 0

    def __init__(self, guest_id, guest_name, room_number, status, start_date, end_date, check_in, check_out, save=True):
        Booking.booking_id += 1
        self.id = Booking.booking_id
        self.guest_id = guest_id
        self.guest_name = guest_name
        self.room_number = room_number
        self.status = status
        self.start_date = start_date
        self.end_date = end_date
        self.check_in = check_in
        self.check_out = check_out
        Booking.booking_registry.append(self)
        if save:
            self.save_to_csv()



    def save_to_csv(self):
        os.makedirs("data", exist_ok=True)
        booking_file_exists = os.path.exists(Booking.file_path)
        with open(Booking.file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if not booking_file_exists:
                writer.writerow([
                    "Booking ID",
                    "Guest ID",
                    "Guest Name",
                    "Room Number",
                    "Status",
                    "Start Date",
                    "End Date",
                    "Check In Timestamp",
                    "Check Out Timestamp",
                ])
            writer.writerow([
                self.id,
                self.guest_id,
                self.guest_name,
                self.room_number,
                self.status,
                self.start_date,
                self.end_date,
                self.check_in,
                self.check_out
            ])

    @classmethod
    def save_after_modification(cls):
        os.makedirs(cls.dir_name, exist_ok=True)

        with open(cls.file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                "Booking ID",
                "Guest ID",
                "Guest Name",
                "Room Number",
                "Status",
                "Start Date",
                "End Date",
                "Check In Timestamp",
                "Check Out Timestamp",
            ])
            for booking in cls.booking_registry:
                writer.writerow([
                    booking.id,
                    booking.guest_id,
                    booking.guest_name,
                    booking.room_number,
                    booking.status,
                    booking.start_date,
                    booking.end_date,
                    booking.check_in,
                    booking.check_out
                ])


def load_booking_data():
    if not os.path.exists(Booking.file_path):
        return
    else:
        with open(Booking.file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                booking = Booking(
                    row["Guest ID"],
                    row["Guest Name"],
                    int(row["Room Number"]),
                    row["Status"],
                    row["Start Date"],
                    row["End Date"],
                    row["Check In Timestamp"],
                    row["Check Out Timestamp"],
                    save=False
                )
                read_booking_id = int(row["Booking ID"])
                Booking.booking_id = max(read_booking_id, Booking.booking_id)  # compares booking from line 6 and the one we loaded from the csv file into memory and re-assigns it to the largest number