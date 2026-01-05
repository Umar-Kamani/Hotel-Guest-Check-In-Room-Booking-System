import csv
import os

class Room:
    room_registry=[]
    dir_name = "data"
    file_name = "rooms.csv"
    file_path = f"{dir_name}/{file_name}"

    def __init__(self, room_number, room_type, room_capacity, room_status, room_condition, room_access_pin, room_rate, save=True):
        self.room_number = room_number
        self.room_type = room_type
        self.room_status = room_status
        self.room_rate = room_rate
        self.room_condition = room_condition
        self.room_access_pin = room_access_pin
        self.room_capacity = room_capacity
        Room.room_registry.append(self)
        if save:
            self.save_to_csv()

    def save_to_csv(self):
        os.makedirs("data", exist_ok=True)
        room_file_exists = os.path.exists(Room.file_path)
        with open(Room.file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if not room_file_exists:
                writer.writerow([
                    "Room Number",
                    "Room Type",
                    "Room Capacity",
                    "Room Status",
                    "Room Condition",
                    "Room Access Pin",
                    "Room Rate"
                ])
            writer.writerow([
                self.room_number,
                self.room_type,
                self.room_capacity,
                self.room_status,
                self.room_condition,
                self.room_access_pin,
                self.room_rate
            ])
def load_room_data():
    if not os.path.exists(Room.file_path):
        return
    else:
        with open(Room.file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                room = Room(
                    int(row["Room Number"]),
                    row["Room Type"],
                    row["Room Capacity"],
                    row["Room Status"],
                    row["Room Condition"],
                    row["Room Access Pin"],
                    row["Room Rate"],
                    save = False
                )
            Room.room_registry.append(room) #Appends all rooms from csv to memory
    return

