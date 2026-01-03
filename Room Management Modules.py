import classes

def create_new_room():
    print("Welcome to the Room Creation Wizard")
    new_room_number=input("Please enter the room number: ")
    while True: #Room type user input check
        print("""Room Types:
              1. Standard Room
              2. Deluxe Room
              3. Suite Room""")
        new_room_type=input("Please select your room type: ")
        if new_room_type == '1':
            new_room_type = "Standard Room"
            print(f"Room Type: {new_room_type}.")
            break
        elif new_room_type == '2':
            new_room_type = "Deluxe Room"
            print(f"Room Type: {new_room_type}.")
            break
        elif new_room_type == '3':
            new_room_type = "Suite Room"
            print(f"Room Type: {new_room_type}.")
            break
        else :
            print("Invalid room type. Please try again.")
    while True:
        new_room_capacity=input("Please enter the room capacity: ")
    while True: #Room condition user input check
        print("""Room Condition:
              1. Clean
              2. Dirty""")
        new_room_condition=input("Please enter the room condition: ")
        if new_room_condition == '1':
            new_room_condition = "Clean"
            print(f"Room Condition: {new_room_condition}")
            break
        elif new_room_condition == '2':
            new_room_condition = "Dirty"
            print(f"Room Condition: {new_room_condition}")
            break
        else :
            print("Invalid room condition. Please try again.")
    new_room_access_pin=input("Please enter the room access pin: ")
    new_room_rate=input("Please enter the room rate: ")

    print(new_room_number)
    print(new_room_type)
    print(new_room_condition)
    print(new_room_access_pin)
    print(new_room_rate)
    print(new_room_capacity)

    new_room = classes.Room(new_room_number, new_room_type,"empty", new_room_rate, new_room_condition , new_room_access_pin, new_room_capacity)

create_new_room()