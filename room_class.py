import csv
import os

class Room:
    room_registry=[]
    room_id = 0
    file_name = "rooms.csv"
    file_path = f"data/{file_name}"

    def __init__(self, room_number, room_type, room_status, room_rate, room_condition, room_access_pin, room_capacity):
        Room.room_id += 1
        self.id = Room.room_id
        self.room_number = room_number
        self.room_type = room_type
        self.room_status = room_status
        self.room_rate = room_rate
        self.room_condition = room_condition
        self.room_access_pin = room_access_pin
        self.room_capacity = room_capacity
        Room.room_registry.append(self)
        self.save_to_csv()

    def save_to_csv(self):
        room_file_exists = os.path.exists(Room.file_path)
        with open(Room.file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if not room_file_exists:
                writer.writerow([
                    "ID",
                    "Room Number",
                    "Room Type",
                    "Room Capacity",
                    "Room Status",
                    "Room Condition",
                    "Room Access Pin",
                    "Room Rate"
                ])
            writer.writerow([
                self.id,
                self.room_number,
                self.room_type,
                self.room_capacity,
                self.room_status,
                self.room_condition,
                self.room_access_pin,
                self.room_rate
            ])
    def load_room_data(self):
        if not os.path.exists(Room.file_path):
            return
        else:
            with open(Room.file_path, 'r') as csvfile:
                reader = csv.reader(csvfile)
                print(reader)

