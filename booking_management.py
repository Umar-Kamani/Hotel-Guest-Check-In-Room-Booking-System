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
        and t.room_status == "Empty"
        and t.room_capacity >= booking_room_capacity
        and not any(
            datetime.strptime(b.start_date,"%Y-%m-%d") < start_date_booking
            and datetime.strptime(b.end_date,"%Y-%m-%d") > end_date_booking
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
                    "Booking Start Date": t.start_date,
                    "Booking End Date": t.end_date
                })
                print(f"The following rooms with type '{booking_room_type}' and capacity '"
                      f"{booking_room_capacity} are available:")
                print(tabulate(available_rooms, headers="keys", tablefmt="fancy_grid"))
    else:
        print(f"No rooms with type '{booking_room_type}' and capacity '{booking_room_capacity} are available\n")
        room_management.view_available_rooms()

    while True:
        booking_room_number = input("Please enter the room number you wish to book: ")
        try:
            booking_room_number = int(booking_room_number)
            break
        except ValueError:
            print("Invalid room number. Please choose an available room.")

        for available in available_room_filter:
            if booking_room_number == available.room_number:
                break
            elif booking_room_number != available.room_number:
                print("Invalid room number. Please choose an available room.")
    while True:
        guest_id_passport_number = input("Please enter the guest ID/Passport number: ")
        if not guest_id_passport_number.strip():
            print("Invalid guest ID/Passport number. Please try again.")
        elif any(guest_id_passport_number == guest.id_passport for guest in guest_class.Guest.guest_registry):
            print("Guest already exist, please find info below.")
            existing_guest=[]
            for t in guest_class.Guest.guest_registry:
                if t.id_passport == guest_id_passport_number:
                    existing_guest.append({
                        "Guest ID": t.guest_id,
                        "Guest Name": t.full_name,
                        "Guest Phone Number": t.phone_number,
                        "Guest Date of Birth": t.birth_date,
                        "Guest ID/Passport": t.id_passport,
                    })
            print(tabulate(existing_guest, headers="keys", tablefmt="fancy_grid"))
            break
        else:
            print("Guest is not yet registered, please proceed to register guest for booking\n")
            guest_management.create_new_guest()
            break

    new_guest_list=[]
    for guest in guest_class.Guest.guest_registry:
        if guest.id_passport == guest_id_passport_number:
            new_guest_pass_id=guest.id_passport
        booking=booking_class.Booking(guest.guest_id, booking_room_number, "Booked", start_date_booking, end_date_booking)

    print("Booking Complete")
    #update memory









room_class.load_room_data()
create_booking()
