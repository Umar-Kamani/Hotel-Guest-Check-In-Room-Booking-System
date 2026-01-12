import booking_class
from tabulate import tabulate
from datetime import datetime

import guest_class
import room_class
import room_management
import guest_management


def create_booking():


    print("___________________________________")
    print("Welcome to the Booking Wizard")
    print("___________________________________")
    #Room type selection
    while True:
        print("""Room Types:
                      1. Standard Room
                      2. Deluxe Room
                      3. Suite Room""")
        booking_room_type = input("Please select the room type you wish to book: ")
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
    #Room capacity selection
    while True:
        booking_room_capacity = input("Please enter the room capacity you wish to book: ")
        try:
            booking_room_capacity = int(booking_room_capacity)
            if not 0 < booking_room_capacity <= 6: #checks validity of room capacity input, max room capacity 6 pax
                print("Invalid room capacity. Please try again, room capacity can't exceeds 6.")
            else:
                break
        except ValueError:
            print("Invalid room capacity. Please try again.")
    #Room booking timeframe input
    while True:
        start_date_booking = input("Please enter the start date of booking (YYYY-MM-DD): ")
        try:
            datetime.strptime(start_date_booking, "%Y-%m-%d")
        except ValueError:
            print("Invalid start date format. Please use YYYY-MM-DD.")
            continue
        if start_date_booking == datetime.now().strftime("%Y-%m-%d"):
            continue
        end_date_booking = input("Please enter the end date of booking (YYYY-MM-DD): ")
        try:
            datetime.strptime(end_date_booking, "%Y-%m-%d")
        except ValueError:
            print("Invalid end date format. Please use YYYY-MM-DD.")
            continue
        if end_date_booking < start_date_booking:
            print("End date cannot be earlier than start date. Please try again.")
            continue
        break

            #Check if room is available
    available_room_filter=[
        t for t in room_class.Room.room_registry
        if t.room_type == booking_room_type
        and t.room_status != "Occupied"
        and t.room_capacity >= booking_room_capacity
        and not any(
            datetime.strptime(b.start_date,"%Y-%m-%d") < datetime.strptime(start_date_booking,"%Y-%m-%d")
            and datetime.strptime(b.end_date,"%Y-%m-%d") > datetime.strptime(end_date_booking, "%Y-%m-%d")
            for b in booking_class.Booking.booking_registry
        )]

    if available_room_filter:
        available_rooms=[]
        for t in available_room_filter:
                available_rooms.append({
                    "Room Number": t.room_number,
                    "Room Type": t.room_type,
                    "Room Capacity": t.room_capacity,
                    "Room Status": t.room_status,
                    "Room Condition": t.room_condition,
                    "Room Rate": f"${t.room_rate}",
                })
                print(f"The following rooms with type '{booking_room_type}' and capacity '"
                      f"{booking_room_capacity} are available:")
                print(tabulate(available_rooms, headers="keys", tablefmt="fancy_grid"))
    else:
        print(f"No rooms with type '{booking_room_type}' and capacity '{booking_room_capacity} are available\n")
        room_management.view_available_rooms()
        create_booking()

    while True:
        booking_room_number = input("Please enter the room number you wish to book: ")
        try:
            booking_room_number = int(booking_room_number)
            if any(booking_room_number == room.room_number for room in available_room_filter):
                break
            else:
                print("Invalid room number. Please choose an available room.")
        except ValueError:
            print("Invalid room number. Please choose an available room.")

    while True:
        guest_id_passport_number = input("Please enter the guest ID/Passport number: ")
        if not guest_id_passport_number.strip():
            print("Invalid guest ID/Passport number. Please try again.")
        elif any(guest_id_passport_number == guest.passport_number for guest in guest_class.Guest.guest_registry):
            print("Guest already exist, please find info below.")
            existing_guest=[]
            for t in guest_class.Guest.guest_registry:
                if t.passport_number == guest_id_passport_number:
                    existing_guest.append({
                        "Guest ID": t.guest_id,
                        "Guest Name": t.full_name,
                        "Guest Phone Number": t.phone_number,
                        "Guest Date of Birth": t.date_of_birth,
                        "Guest ID/Passport": t.passport_number,
                    })
            print(tabulate(existing_guest, headers="keys", tablefmt="fancy_grid"))
            break
        else:
            print("Guest is not yet registered, please proceed to register guest for booking\n")
            guest_management.create_new_guest()
            break

    new_guest_list=[]
    for guest in guest_class.Guest.guest_registry:
        if guest.passport_number == guest_id_passport_number:
            booking=booking_class.Booking(guest.guest_id, guest.full_name, booking_room_number, "Booked", start_date_booking, end_date_booking)

    new_booking_filter=[t for t in booking_class.Booking.booking_registry]
    new_booking=[]
    for t in new_booking_filter:
        if t.start_date == start_date_booking:
            new_booking.append({
                "Booking ID": t.id,
                "Guest ID": t.guest_id,
                "Guest Name": t.guest_name,
                "Guest Room Number": t.room_number,
                "Booking Status": t.status,
                "Booking Start Date": t.start_date,
                "Booking End Date": t.end_date
            })
    print("Booking Complete, please find booking info below.")
    print(tabulate(new_booking, headers="keys", tablefmt="fancy_grid"))

    #update the status of the booked room
    for t in room_class.Room.room_registry:
        if t.room_number == booking_room_number:
            t.room_status = "Booked"
            room_class.Room.save_after_modification()




room_class.load_room_data()
guest_class.load_guest_data()
booking_class.load_booking_data()
create_booking()
