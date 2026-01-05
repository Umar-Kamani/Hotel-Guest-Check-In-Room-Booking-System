class Guest:
    def __init__(self, guest_id, full_name, phone_number, id_number, date_of_birth):
        self.guest_id = guest_id
        self.full_name = full_name
        self.phone_number = phone_number
        self.id_number = id_number
        self.date_of_birth = date_of_birth
        self.validate()

 def __str__(self):
        return f"Guest[{self.guest_id}] - {self.full_name}"

        #This is to validate guest data
def validate(self):
        if not self.guest_id:
            raise ValueError("Guest ID is required")
        if not self.full_name or len(self.full_name.strip()) == 0:
            raise ValueError("Full name is required")
        if not self.phone_number:
            raise ValueError("Phone number is required")
        if not self.id_number:
            raise ValueError("ID number is required")
        if not self.date_of_birth:
            raise ValueError("Date of birth is required")
        
        # Basic phone number validation (should contain digits)
        if not any(char.isdigit() for char in self.phone_number):
            raise ValueError("Phone number must contain digits")

    def to_dict(self):
        # Convert guest details to dictionary for saving to file.
        return {
            "guest_id": self.guest_id,
            "full_name": self.full_name,
            "phone_number": self.phone_number,
            "id_number": self.id_number,
            "date_of_birth": self.date_of_birth
        }

   

