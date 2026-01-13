import booking_class
import booking_management
import guest_class
import room_class
import room_management

print("Loading data...")
room_class.load_room_data()
print("Room Data Loaded Successfully...")
guest_class.load_guest_data()
print("Guest Data Loaded Successfully...")
booking_class.load_booking_data()
print("Booking Data Loaded Successfully...")
print("All Data has been successfully loaded!!!"
      "System is Ready")

def main_menu():
    print("Welcome to Room Booking System Main Menu")
    print("1. Check In Guest")
    print("2. Check Out Guest")
    print("3. Booking Management Menu")
    print("4. Room Management Menu")
    print("5. Guest Management Menu")
    print("6. Exit")
    while True:  # This loop checks for correct user choice input
     main_menu_choice = input("Enter your choice: ")
     if main_menu_choice not in ('1', '2', '3', '4', '5', '6', 'exit'):
         print("Invalid choice. Please try again.")
     else:
         break
    if main_menu_choice == '1':
        booking_management.check_in_booking()
    elif main_menu_choice == '2':
        booking_management.check_out_booking()
    elif main_menu_choice == '3':
        booking_management_menu()
    elif main_menu_choice == '4':
        room_management_menu()
    elif main_menu_choice == '5':
        guest_management_menu()
    elif main_menu_choice == '6' or main_menu_choice == 'exit':
         print("Thank you.")
         exit()

def booking_management_menu():
    print("Welcome to Booking Management Menu")
    print("1. Create booking.")
    print("2. Cancel booking.")
    print("3. Exit")
    while True:  # This loop checks for correct user choice input
        booking_menu_choice = input("Enter your choice: ").lower()
        if booking_menu_choice not in ('1', '2', '3', 'exit'):
            print("Invalid choice. Please try again.")
        else:
            break
    if booking_menu_choice == '1':
        booking_management.create_booking()
    elif booking_menu_choice == '2':
        booking_management.delete_booking()
    else:
        print("Thank you.")
    return main_menu()

def room_management_menu():
    print("Welcome to Room Management Menu")
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
        if room_menu_choice not in ('1', '2', '3', '4', '5', '6', '7', '8' or 'exit'):
            print("Invalid choice. Please try again.")
        else:
            break
    if room_menu_choice == '1':
        room_management.view_all_rooms()
    elif room_menu_choice == '2':
        room_management.view_specific_room()
    elif room_menu_choice == '3':
        room_management.view_available_rooms()
    elif room_menu_choice == '4':
        room_management.view_occupied_rooms()
    elif room_menu_choice == '5':
        room_management.create_new_room()
    elif room_menu_choice == '6':
        room_management.delete_room()
    elif room_menu_choice == '7':
        room_management.modify_room()
    elif room_menu_choice == '8' or room_menu_choice == 'exit':
        print("Thank you.")
    return main_menu()

def guest_management_menu():
    print("Welcome to Guest Management Menu")
