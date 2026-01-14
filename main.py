import booking_class
import booking_management
import guest_class
import guest_management
import room_class
import room_management


room_class.load_room_data()
print("Room Data Loaded Successfully")
print("---------------------------------")

guest_class.load_guest_data()
print("Guest Data Loaded Successfully")
print("---------------------------------")

booking_class.load_booking_data()
print("Booking Data Loaded Successfully")
print("---------------------------------")
print("All Data has been successfully loaded!!!"
      "System is Ready\n\n\n")
def main_menu():
    print("Welcome to Hotel Management System")
    print("----------------------------------")
    print("1. Check In Guest")
    print("2. Check Out Guest")
    print("3. Booking Management Menu")
    print("4. Room Management Menu")
    print("5. Guest Management Menu")
    print("6. Exit")
    while True:  # This loop checks for correct user choice input
     main_menu_choice = input("Enter your choice: ").lower()
     if main_menu_choice not in ('1', '2', '3', '4', '5', '6', 'exit'):
         print("Invalid choice. Please try again.")
     else:
         break
    if main_menu_choice == '1':
        booking_management.check_in_booking()
        return main_menu()

    elif main_menu_choice == '2':
        booking_management.check_out_booking()
        return main_menu()

    elif main_menu_choice == '3':
        booking_management_menu()
        return main_menu()

    elif main_menu_choice == '4':
        room_management_menu()
        return main_menu()

    elif main_menu_choice == '5':
        guest_management_menu()
        return main_menu()

    else:
         print("Thank you.")
         exit()

def booking_management_menu():
    print("Welcome to Booking Management Menu")
    print("----------------------------------")
    print("1. Create booking.")
    print("2. Cancel booking.")
    print("3. Check In Guest")
    print("4. Check Out Guest")
    print("5. View all bookings.")
    print("6. View specific booking.")
    print("7. Exit")
    while True:  # This loop checks for correct user choice input
        booking_menu_choice = input("Enter your choice: ").lower()
        if booking_menu_choice not in ('1', '2', '3', '4', '5', '6', '7', 'exit'):
            print("Invalid choice. Please try again.")
        else:
            break
    if booking_menu_choice == '1':
        booking_management.create_booking()
        return booking_management_menu()

    elif booking_menu_choice == '2':
        booking_management.delete_booking()
        return booking_management_menu()

    elif booking_menu_choice == '3':
        booking_management.check_in_booking()
        return booking_management_menu()

    elif booking_menu_choice == '4':
        booking_management.check_out_booking()
        return booking_management_menu()

    elif booking_menu_choice == '5':
        booking_management.view_all_bookings()
        return booking_management_menu()

    elif booking_menu_choice == '6':
        booking_management.view_specific_booking()
        return booking_management_menu()

    else:
        print("Thank you.")
    return main_menu()

def room_management_menu():
    print("Welcome to Room Management Menu")
    print("-------------------------------")
    print("1. View all rooms.")
    print("2. View specific room.")
    print("3. View available rooms.")
    print("4. View occupied/Booked rooms.")
    print("5. Create new room.")
    print("6. Delete room.")
    print("7. Modify room.")
    print("8. Exit")
    while True:  # This loop checks for correct user choice input
        room_menu_choice = input("Enter your choice: ").lower()
        if room_menu_choice not in ('1', '2', '3', '4', '5', '6', '7', '8','exit'):
            print("Invalid choice. Please try again.")
        else:
            break
    if room_menu_choice == '1':
        room_management.view_all_rooms()
        return room_management_menu()

    elif room_menu_choice == '2':
        room_management.view_specific_room()
        return room_management_menu()

    elif room_menu_choice == '3':
        room_management.view_available_rooms()
        return room_management_menu()

    elif room_menu_choice == '4':
        room_management.view_occupied_rooms()
        return room_management_menu()

    elif room_menu_choice == '5':
        room_management.create_new_room()
        return room_management_menu()

    elif room_menu_choice == '6':
        room_management.delete_room()
        return room_management_menu()

    elif room_menu_choice == '7':
        room_management.modify_room()
        return room_management_menu()

    elif room_menu_choice == '8' or room_menu_choice == 'exit':
        print("Thank you.")
    return main_menu()

def guest_management_menu():
    print("Welcome to Guest Management Menu")
    print("--------------------------------")
    print("1. View all guests.")
    print("2. View specific guest.")
    print("3. Create new guest.")
    print("4. Modify guest.")
    print("5. Delete guest.")
    print("6. Exit")
    while True:  # This loop checks for correct user choice input
        guest_menu_choice = input("Enter your choice: ").lower()
        if guest_menu_choice not in ('1', '2', '3', '4', '5', '6','exit'):
            print("Invalid choice. Please try again.")
        else:
            break
    if guest_menu_choice == '1':
        guest_management.view_all_guests()
        return guest_management_menu()

    elif guest_menu_choice == '2':
        guest_management.view_specific_guest()
        return guest_management_menu()

    elif guest_menu_choice == '3':
        guest_management.create_new_guest()
        return guest_management_menu()

    elif guest_menu_choice == '4':
        guest_management.modify_guest()
        return guest_management_menu()

    elif guest_menu_choice == '5':
        guest_management.delete_guest()
        return guest_management_menu()

    else:
        print("Thank you.")
        return main_menu()

print(r"""
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  ____  ____  | || |     ____     | || |  _________   | || |  _________   | || |   _____      | || |     _____    | || |      __      | |
| | |_   ||   _| | || |   .'    `.   | || | |  _   _  |  | || | |_   ___  |  | || |  |_   _|     | || |    |_   _|   | || |     /  \     | |
| |   | |__| |   | || |  /  .--.  \  | || | |_/ | | \_|  | || |   | |_  \_|  | || |    | |       | || |      | |     | || |    / /\ \    | |
| |   |  __  |   | || |  | |    | |  | || |     | |      | || |   |  _|  _   | || |    | |   _   | || |      | |     | || |   / ____ \   | |
| |  _| |  | |_  | || |  \  `--'  /  | || |    _| |_     | || |  _| |___/ |  | || |   _| |__/ |  | || |     _| |_    | || | _/ /    \ \_ | |
| | |____||____| | || |   `.____.'   | || |   |_____|    | || | |_________|  | || |  |________|  | || |    |_____|   | || ||____|  |____|| |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
""")
main_menu()