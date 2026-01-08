import os
import csv


class Booking:
    booking_registry = []
    dir_name = "data"
    file_name = "bookings.csv"
    file_path = f"{dir_name}/{file_name}"

    def __init__(self, booking_id, guest_id, room_number, status, start_date, end_date, save=True):
        self.booking_id = booking_id
        self.guest_id = guest_id
        self.room_number = room_number
        self.status = status
        self.start_date = start_date
        self.end_date = end_date
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
                    "Room Number",
                    "Status",
                    "Start Date",
                    "End Date",
                ])
            writer.writerow([
                self.booking_id,
                self.guest_id,
                self.room_number,
                self.status,
                self.start_date,
                self.end_date,
            ])

    @classmethod
    def save_after_modification(cls):
        os.makedirs(cls.dir_name, exist_ok=True)

        with open(cls.file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                "Booking ID",
                "Guest ID",
                "Room Number",
                "Status",
                "Start Date",
                "End Date",
            ])
            for booking in cls.booking_registry:
                writer.writerow([
                    booking.booking_id,
                    booking.guest_id,
                    booking.room_number,
                    booking.status,
                    booking.start_date,
                    booking.end_date,
                ])


def load_booking_data():
    if not os.path.exists(Booking.file_path):
        return
    else:
        with open(Booking.file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                booking = Booking(
                    row["Booking ID"],
                    row["Guest ID"],
                    row["Room Number"],
                    row["Status"],
                    row["Start Date"],
                    row["End Date"],
                    save=False
                )
