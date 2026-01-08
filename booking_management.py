import booking_class
from tabulate import tabulate

import room_class


def create_booking():
    print("___________________________________")
    print("Welcome to the Room Creation Wizard")
    print("___________________________________")
    while True:
        print("""Room Types:
                      1. Standard Room
                      2. Deluxe Room
                      3. Suite Room""")
        booking_room_type = input("Please select the room type you wish to book: ")
        booking_room_capacity = input("Please enter the room capacity you wish to book: ")
        if booking_room_type == '1':
            booking_room_type = "Standard Room"
            break
        if booking_room_type == '2':
            booking_room_type = "Deluxe Room"
            break
        if booking_room_type == '3':
            booking_room_type = "Suite Room"
            break
        else:
            print("Invalid room type. Please try again.")
    #Check if room_type is available
    available_room_filter=[t for t in room_class.Room.room_registry if t.room_type == booking_room_type and t.room_status == "Empty"]
    if available_room_filter:
        available_rooms=[]
        for t in available_room_filter:
                available_rooms.append({
                    "Room Number": t.room_number,
                    "Room Type": t.room_type,
                    "Room Status": t.room_status
                })
                print(f"The following rooms with type '{booking_room_type}' are available:")
                print(tabulate(available_rooms, headers="keys", tablefmt="fancy_grid"))
    else:
        print(f"No rooms with type '{booking_room_type}' are available")




room_class.load_room_data()
create_booking()
