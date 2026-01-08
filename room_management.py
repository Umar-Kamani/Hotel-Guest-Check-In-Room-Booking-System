import room_class
from tabulate import tabulate


def create_new_room():
    print("___________________________________")
    print("Welcome to the Room Creation Wizard")
    print("___________________________________")
    room_status = "Empty"
    #Room number input
    while True:
        room_number=input("Please enter the room number: ") #Asks the user for the room number
        try:
            room_number = int(room_number) #need to make into int to check for duplicates when loading from csv
            if room_number < 1:
                print("Please enter a number greater than 0")
                continue
        except ValueError:
            print("Room number must be a number. Please try again.")
            continue
        if any(room.room_number == room_number for room in room_class.Room.room_registry):
            print("Room number is already taken. Please try again.")
        else:
            break

    print("___________________________________")
    #Room type input
    while True: #this loop enables us to validate the correct choice from the user in terms of room types
        print("""Room Types:
              1. Standard Room
              2. Deluxe Room
              3. Suite Room""")
        room_type=input("Please select your room type: ") #we prompt the user to enter a number according to the room type
        if room_type == '1':
            room_type = "Standard Room"
            print(f"Room Type: {room_type}.")
            break
        elif room_type == '2':
            room_type = "Deluxe Room"
            print(f"Room Type: {room_type}.")
            break
        elif room_type == '3':
            room_type = "Suite Room"
            print(f"Room Type: {room_type}.")
            break
        else :
            print("Invalid room type. Please try again.")

    print("___________________________________")
    #Room capacity input
    while True:
        room_capacity=input("Please enter the room capacity: ")
        try:
            room_capacity = int(room_capacity)
            if not 0 < room_capacity <= 6: #checks validity of room capacity input, max room capacity 6 pax
                print("Invalid room capacity. Please try again, room capacity can't exceeds 6.")
            else:
                break
        except ValueError:
            print("Invalid room capacity. Please try again.")

    print("___________________________________")
    #Room condition input
    while True: #this loop enables us to validate the correct choice from the user in terms of room condition
        print("""Room Condition:
              1. Clean
              2. Dirty""")
        room_condition=input("Please enter the room condition: ")
        if room_condition == '1':
            room_condition = "Clean"
            print(f"Room Condition: {room_condition}")
            break
        elif room_condition == '2':
            room_condition = "Dirty"
            print(f"Room Condition: {room_condition}")
            break
        else :
            print("Invalid room condition. Please try again.")

    print("___________________________________")
    #Room Access Pin input
    while True:
        room_access_pin=input("Please enter the room access pin: ")
        try:
            if not room_access_pin.isdigit() or len(room_access_pin) != 4: #this function checks for a valid 4 digit access pin
                print("Invalid room access pin. Room access pin must be 4 digits long.")
            else:
                break
        except ValueError:
            print("Invalid room access pin. Room access pin must be 4 digits long.")

    print("___________________________________")
    #Room Rate input
    while True:
        room_rate=input("Please enter the room rate: $")
        try:
            room_rate = float(room_rate)
            if room_rate <= 0:
                print("Invalid room rate. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid room rate. Please try again.")

    print("___________________________________")
    room = room_class.Room(room_number, room_type, room_capacity, room_status, room_condition, room_access_pin, room_rate) #makes new room into an object
    print("___________________________________________________________")
    print("Room Successfully Created, please verify room details below:\n")
    room_data = {
        "Room Number": room_number,
        "Room Type": room_type,
        "Room Capacity": room_capacity,
        "Room Status": room_status,
        "Room Condition": room_condition,
        "Room Access Pin": room_access_pin,
        "Room Rate ($)": room_rate,
    }
    print(tabulate([room_data], headers="keys", tablefmt="fancy_grid"))

def modify_room():
    print("___________________________________")
    print("Welcome to the Room Modification Menu")
    print("___________________________________")
    while True:
        room_num_modify = input("Please enter the room number of the room you want to modify: ")
        try:
            room_num_modify = int(room_num_modify)
            if any(room.room_number == room_num_modify for room in room_class.Room.room_registry):
                break
            else:
                print("Room doesn't exist. Please enter a valid room number.")
        except ValueError:
            print("Invalid room number. Please try again.")

    old_room_filter=[t for t in room_class.Room.room_registry if t.room_number == room_num_modify]
    old_room_list=[]

    for t in old_room_filter:
        if t.room_number == room_num_modify:
            old_room_list.append({
                "Room Number": t.room_number,
                "Room Type": t.room_type,
                "Room Capacity": t.room_capacity,
                "Room Status": t.room_status,
                "Room Condition": t.room_condition,
                "Room Access Pin": t.room_access_pin,
                "Room Rate ($)": t.room_rate,
            })

    print("\nPlease verify room details below:")
    print(tabulate(old_room_list, headers="keys", tablefmt="fancy_grid"))
    print("Room Details")
    print("1. Room Number")
    print("2. Room Type")
    print("3. Room Capacity")
    print("4. Room Status")
    print("5. Room Condition")
    print("6. Room Access Pin")
    print("7. Room Rate ($)")
    print("8. Exit")
    while True:
        details_modify = input("Please select room details to modify: ")
        if details_modify not in ('1', '2', '3', '4', '5', '6', '7', '8', 'exit'):
            print("Invalid choice. Please try again.")
        else:
            break
    if details_modify == '1':
        edit_room_number(room_num_modify)
    elif details_modify == '2':
        edit_room_type(room_num_modify)
    elif details_modify == '3':
        edit_room_capacity(room_num_modify)
    elif details_modify == '4':
        edit_room_status(room_num_modify)
    elif details_modify == '5':
        edit_room_condition(room_num_modify)
    elif details_modify == '6':
        edit_room_access_pin(room_num_modify)
    elif details_modify == '7':
        edit_room_rate(room_num_modify)
    else:
        return


def edit_room_number(room_num_modify):
    while True:
        new_room_number = input("Please enter the new room number: ")
        if any(room.room_number == new_room_number for room in room_class.Room.room_registry):
            print("Room Number already exists. Please enter a new room number.")
        else:
            try:
                new_room_number = int(new_room_number)
                break
            except ValueError:
                print("Invalid room number. Please try again.")

    for t in room_class.Room.room_registry:
        if t.room_number == room_num_modify:
            t.room_number = new_room_number
            room_class.Room.save_after_modification()
            print("Room Number Updated")
            view_modified_room(new_room_number)


def edit_room_type(room_num_modify):
    while True:
        print("""Room Types:
                      1. Standard Room
                      2. Deluxe Room
                      3. Suite Room""")
        new_room_type = input("Please select new room type: ")
        if new_room_type == '1':
            new_room_type = "Standard Room"
            print(f"Room Type '{new_room_type}' selected.")
            break
        elif new_room_type == '2':
            new_room_type = "Deluxe Room"
            print(f"Room Type '{new_room_type}' selected.")
            break
        elif new_room_type == '3':
            new_room_type = "Suite Room"
            print(f"Room Type '{new_room_type}' selected.")
            break
        else:
            print("Invalid room type. Please try again.")

    for t in room_class.Room.room_registry:
        if t.room_number == room_num_modify:
            t.room_type = new_room_type
            room_class.Room.save_after_modification()
            print("Room Type Updated")
    view_modified_room(room_num_modify)
    
def edit_room_capacity(room_num_modify):
    while True:
        new_room_capacity = input("Please enter the room capacity: ")
        try:
            new_room_capacity = int(new_room_capacity)
        except ValueError:
            print("Invalid room capacity. Please try again.")
        if not 0 < new_room_capacity <= 6:  # checks validity of room capacity input, max room capacity 6 pax
            print("Invalid room capacity. Please try again, room capacity can't exceeds 6.")
        else:
            break

    for t in room_class.Room.room_registry:
        if t.room_number == room_num_modify:
            t.room_capacity = new_room_capacity
            room_class.Room.save_after_modification()
            print("Room Type Updated")
    view_modified_room(room_num_modify)

def edit_room_status(room_num_modify):
    while True:
        print("""Room Status:
                      1. Empty
                      2. Booked
                      3. Occupied""")
        new_room_status = input("Please enter the room status: ")
        if new_room_status == '1':
            new_room_status = "Empty"
            print(f"Room Status '{new_room_status}' selected.")
            break
        elif new_room_status == '2':
            new_room_status = "Booked"
            print(f"Room Status '{new_room_status}' selected.")
            break
        elif new_room_status == '3':
            new_room_status = "Occupied"
            print(f"Room Status '{new_room_status}' selected.")
            break
        else:
            print("Invalid room Status. Please try again.")

        for t in room_class.Room.room_registry:
            if t.room_number == room_num_modify:
                t.room_status = new_room_status
                room_class.Room.save_after_modification()
                print("Room Status Updated")
        view_modified_room(room_num_modify)

def edit_room_condition(room_num_modify):
    while True:
        print("""Room Condition:
                      1. Clean
                      2. Dirty""")
        new_room_condition = input("Please enter the room condition: ")
        if new_room_condition == '1':
            new_room_condition = "Clean"
            print(f"Room Condition '{new_room_condition}' selected.")
            break
        elif new_room_condition == '2':
            new_room_condition = "Dirty"
            print(f"Room Condition '{new_room_condition}' selected.")
            break
        else:
            print("Invalid room condition. Please try again.")

    for t in room_class.Room.room_registry:
        if t.room_number == room_num_modify:
            t.room_condition = new_room_condition
            room_class.Room.save_after_modification()
            print("Room Condition Updated")
    view_modified_room(room_num_modify)

def edit_room_access_pin(room_num_modify):
    while True:
        new_room_access_pin = input("Please enter the room access pin: ")
        try:
            if not new_room_access_pin.isdigit() or len(new_room_access_pin) != 4:  # this function checks for a valid 4 digit access pin
                print("Invalid room access pin. Room access pin must be 4 digits long.")
            else:
                break
        except ValueError:
            print("Invalid room access pin. Room access pin must be 4 digits long.")

    for t in room_class.Room.room_registry:
        if t.room_number == room_num_modify:
            t.room_access_pin = new_room_access_pin
            room_class.Room.save_after_modification()
            print("Room Access Pin Updated")
    view_modified_room(room_num_modify)

def edit_room_rate(room_num_modify):
    while True:
        new_room_rate=input("Please enter the room rate: $")
        try:
            new_room_rate = float(new_room_rate)
            if new_room_rate <= 0:
                print("Invalid room rate. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid room rate. Please try again.")

    for t in room_class.Room.room_registry:
        if t.room_number == room_num_modify:
            t.room_rate = new_room_rate
            room_class.Room.save_after_modification()
            print("Room Rate Updated")
    view_modified_room(room_num_modify)

def delete_room():
    while True:
        delete_room_num = input("Please enter the room number of the room you want to delete: ")
        try:
            delete_room_num = int(delete_room_num)
            if any(room.room_number == delete_room_num for room in room_class.Room.room_registry):
                break
            else:
                print("Room doesn't exist. Please enter a valid room number.")
        except ValueError:
            print("Invalid room number. Please try again.")

    for t in room_class.Room.room_registry:
        if t.room_number == delete_room_num:
            room_class.Room.room_registry.remove(t)
            room_class.Room.save_after_modification()
            print("Room Deleted Successfully")

def view_modified_room(modified_room_number):
    view_room=[]
    for room in room_class.Room.room_registry:
        if room.room_number == modified_room_number:
            view_room.append({
                "Room Number": room.room_number,
                "Room Type": room.room_type,
                "Room Capacity": room.room_capacity,
                "Room Status": room.room_status,
                "Room Condition": room.room_condition,
                "Room Access Pin": room.room_access_pin,
                "Room Rate ($)": room.room_rate,
            })
    print(tabulate(view_room, headers="keys", tablefmt="fancy_grid"))

def view_all_rooms():
    all_rooms = []
    for room in room_class.Room.room_registry:
        all_rooms.append({
            "Room Number": room.room_number,
            "Room Type": room.room_type,
            "Room Capacity": room.room_capacity,
            "Room Status": room.room_status,
            "Room Condition": room.room_condition,
            "Room Access Pin": room.room_access_pin,
            "Room Rate ($)": room.room_rate,
        })
    print(tabulate(all_rooms, headers="keys", tablefmt="fancy_grid"))

def view_specific_room():
    while True:
        view_room_number = input("Please enter the room number of the room you want to view: ")
        try:
            view_room_number = int(view_room_number)
            if any(room.room_number == view_room_number for room in room_class.Room.room_registry):
                break
            else:
                print("Room doesn't exist. Please enter a valid room number.")
        except ValueError:
            print("Invalid room number. Please try again.")
    specific_room_list = []

    for room in room_class.Room.room_registry:
        if room.room_number == view_room_number:
            specific_room_list.append({
                "Room Number": room.room_number,
                "Room Type": room.room_type,
                "Room Capacity": room.room_capacity,
                "Room Status": room.room_status,
                "Room Condition": room.room_condition,
                "Room Access Pin": room.room_access_pin,
                "Room Rate ($)": room.room_rate,
            })
    print(f"Please find all details about room {view_room_number} below.")
    print(tabulate(specific_room_list, headers="keys", tablefmt="fancy_grid"))

def view_available_rooms():
    available_rooms = []
    for room in room_class.Room.room_registry:
        if room.room_status == "Empty":
            available_rooms.append({
                "Room Number": room.room_number,
                "Room Type": room.room_type,
                "Room Capacity": room.room_capacity,
                "Room Status": room.room_status,
                "Room Condition": room.room_condition,
                "Room Access Pin": room.room_access_pin,
                "Room Rate ($)": room.room_rate,
            })
    print(f"Please find all available rooms below.")
    print(tabulate(available_rooms, headers="keys", tablefmt="fancy_grid"))

def view_occupied_rooms():
    occupied_rooms = []
    for room in room_class.Room.room_registry:
        if room.room_status == "Occupied" or "Booked":
            occupied_rooms.append({
                "Room Number": room.room_number,
                "Room Type": room.room_type,
                "Room Capacity": room.room_capacity,
                "Room Status": room.room_status,
                "Room Condition": room.room_condition,
                "Room Access Pin": room.room_access_pin,
                "Room Rate ($)": room.room_rate,
            })
    print(f"Please find all Occupied or Booked rooms below.")
    print(tabulate(occupied_rooms, headers="keys", tablefmt="fancy_grid"))

