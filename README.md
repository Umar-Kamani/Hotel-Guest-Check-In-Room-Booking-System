# Hotel-Guest-Check-In-Room-Booking-System

OVERVIEW
-
This project is a hotel management system built with Python. It is designed to streamline and automate essential hotel operations by addressing common challenges. 
The system focuses on:

1. Managing and storing guest information securely.
2. Tracking room availability and conditions in real time.
3. Handling reservations and cancellations efficiently.
4. Supporting smooth check-in and check-out processes with accurate timestamps.
5. Persisting hotel data using CSV files to ensure data is not lost when the program closes.

By using modular design with persistent CSV-based storage, the system ensures that hotel staff can manage daily operations in a clear, organized, and user-friendly manner. This solution aims to provide a practical solution that improves efficiency, reduces manual errors, and keeps hotel records well-structured. This is to help reduce wait time in booking hotels.

Project Structure
-
The project is organized into multiple Python files, each responsible for a specific part of the hotel management system. This includes:
1. `main.py`
    -
- Loads all saved data from CSV files (rooms, guests, bookings) into memory when the program starts.

- Displays the main menu and controls navigation across all the python files and all the entire system. ![img.png](img.png)

- Connects all modules together (Guest, Room, Booking).
- Ensures smooth transitions between management menus.
- Has input validation to prevent invalid or duplicate records.
- Contains tabulated data display for easy readability.

- It has main menu options which includes:
    * Guest check-in.

    * Guest check-out.

    * Booking management menu.

    * Room management menu.

    * Guest management menu.

    * Exit system.
2. `guest class.py`:
   -
- It defines the guest class
- It has key Attributes such as:
   - Guest ID (auto-generated).
   - Full name.  
   - Phone number.  
   - Date of birth.  
   - Passport/ID number. 
- It loads guest data into memory (`guest_registry`)
- It provides `save_after_modification()` to update CSV after edits.

3. `guest management`:
   -
- It provides interactive  functions for managing guests. 
- It has key features such as: 
    1. `Create new guest` which validates passport, name, phone, and DOB.  
    2. `Modify guest details`: Edit name, phone, DOB, or passport number.  
    3. `View all guests`: Displays all registered guests in tabulated format.  
    4. `View specific guest`:This allows one to search for guest by passport number.  
- It saves all changes to guests.cv


4. `room class.py`:
    -
- This python file defines the Guest class and handles guest data storage.
- It auto-generates a unique Guest ID for each guest.
- It stores guest details such as:
   - Guest ID (auto-generated).
   - Full name. 
   - Phone number. 
   - Date of birth. 
   - Passport/ID number.
-**Key features include:**

    * `Create New Guest`: This validates passport/ID uniqueness, makes sure names contain only letters and validates phone numbers and date of birth.
    * `Modify Guest Details`: Provides options to edit full name, phone number, date of birth and Passport/ID number.
    * `View All Guests` : Displays all registered guests in a table form.
    * `View Specific Guest` : Searches and displays guest details using passport/ID number.
    * `Delete Guest` : Removes guest from memory and updates the CSV.


    

