import classes

def create_new_room():
    print("Welcome to the Room Creation Wizard")
    #Room number input
    while True:
        new_room_number=input("Please enter the room number: ") #Asks the user for the room number
        if new_room_number == "":
            print("Please enter a valid room number.")
        else:
            break
    #Room type input
    while True: #this loop enables us to validate the correct choice from the user in terms of room types
        print("""Room Types:
              1. Standard Room
              2. Deluxe Room
              3. Suite Room""")
        new_room_type=input("Please select your room type: ") #we prompt the user to enter a number according to the room type
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
    #Room capacity input
    while True:
        new_room_capacity=input("Please enter the room capacity: ")
        try:
            new_room_capacity = int(new_room_capacity)
            if new_room_capacity == "" or new_room_capacity >= 6: #checks validity of room capacity input, max room capacity 6 pax
                print("Invalid room capacity. Please try again, room capacity can't exceeds 6.")
            else:
                break
        except ValueError:
            print("Invalid room capacity. Please try again.")
    #Room condition input
    while True: #this loop enables us to validate the correct choice from the user in terms of room condition
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
    #Room Access Pin input
    while True:
        new_room_access_pin=input("Please enter the room access pin: ")
        try:
            if not new_room_access_pin.isdigit or new_room_access_pin != 4 or new_room_access_pin == '': #this function checks for a valid 4 digit access pin
                print("Invalid room access pin. Room access pin must be 4 digits long.")
            else:
                break
        except ValueError:
            print("Invalid room access pin. Room access pin must be 4 digits long.")
    #Room Rate input
    while True:
        new_room_rate=input("Please enter the room rate: $")
        if not new_room_rate.isdigit() or new_room_rate == '':
            print("Invalid room rate. Please try again.")
        else:
            break

    print(new_room_number)
    print(new_room_type)
    print(new_room_condition)
    print(new_room_access_pin)
    print(new_room_rate)
    print(new_room_capacity)

    new_room = classes.Room(new_room_number, new_room_type,"empty", new_room_rate, new_room_condition , new_room_access_pin, new_room_capacity)

create_new_room()