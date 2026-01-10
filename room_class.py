import csv
import os
from datetime import datetime

class Room:
    room_registry=[] #memory to store room data
    dir_name = "data" #directory name of room.csv file
    file_name = "rooms.csv" #name of csv file
    file_path = f"{dir_name}/{file_name}" #path of rooms.csv file

    def __init__(self, room_number, room_type, room_capacity, room_status, room_condition, room_access_pin, room_rate, start_date, end_date,
                 save=True):
        self.room_number = room_number
        self.room_type = room_type
        self.room_status = room_status
        self.room_rate = room_rate
        self.room_condition = room_condition
        self.room_access_pin = room_access_pin
        self.room_capacity = room_capacity
        self.start_date = start_date
        self.end_date = end_date
        Room.room_registry.append(self) #Automatically appends any room objects to the room_registry list
        if save: #This statement prevents the program from saving to the rooms.csv file twice
            self.save_to_csv()

    def save_to_csv(self): #method to save data from memory into the rooms.csv file
        os.makedirs("data", exist_ok=True) #Creates directory if it doesn't exist
        room_file_exists = os.path.exists(Room.file_path) #Checks if the room.csv exists and stores the result as a boolean
        with open(Room.file_path, 'a', newline='') as csvfile: #writes data to rooms.csv file
            writer = csv.writer(csvfile)
            if not room_file_exists: #if room_file_exist is False, header row is added
                writer.writerow([
                    "Room Number",
                    "Room Type",
                    "Room Capacity",
                    "Room Status",
                    "Room Condition",
                    "Room Access Pin",
                    "Room Rate",
                    "Start Date",
                    "End Date"
                ])
            writer.writerow([
                self.room_number,
                self.room_type,
                self.room_capacity,
                self.room_status,
                self.room_condition,
                self.room_access_pin,
                self.room_rate,
                self.start_date,
                self.end_date
            ])

    @classmethod #enables us to import class parameters and use them into this function
    def save_after_modification(cls): # This function enables us to save any modifications made to a room back to its correct entry in the csv file
        os.makedirs(cls.dir_name, exist_ok=True) #fail-safe

        with open(cls.file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                "Room Number",
                "Room Type",
                "Room Capacity",
                "Room Status",
                "Room Condition",
                "Room Access Pin",
                "Room Rate",
                "Start Date",
                "End Date"
            ])

            for room in cls.room_registry:
                writer.writerow([
                    room.room_number,
                    room.room_type,
                    room.room_capacity,
                    room.room_status,
                    room.room_condition,
                    room.room_access_pin,
                    room.room_rate,
                    room.start_date,
                    room.end_date
                ])

def load_room_data():
    if not os.path.exists(Room.file_path): #checks if the rooms.csv file exist, if it doesn't it doesn't try to load us the room data into memory
        return
    else: #loads room data into memory so that program is responsive and enables us to use the room_registry to check for data instead of always going to the csv file
        with open(Room.file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                room = Room(
                    int(row["Room Number"]),
                    row["Room Type"],
                    int(row["Room Capacity"]),
                    row["Room Status"],
                    row["Room Condition"],
                    int(row["Room Access Pin"]),
                    float(row["Room Rate"]),
                    row["Start Date"],
                    row["End Date"],
                    save = False
                )
    return