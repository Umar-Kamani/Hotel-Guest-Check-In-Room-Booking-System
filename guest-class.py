class Guest:
    def __init__(self, guest_id, full_name, phone_number, id_number, date_of_birth):
        self.guest_id = guest_id
        self.full_name = full_name
        self.phone_number = phone_number
        self.id_number = id_number
        self.date_of_birth = date_of_birth

 def __str__(self):
        return f"Guest[{self.guest_id}] - {self.full_name}"

    def to_dict(self):
        # Convert guest details to dictionary for saving to file.
        return {
            "guest_id": self.guest_id,
            "full_name": self.full_name,
            "phone_number": self.phone_number,
            "id_number": self.id_number,
            "date_of_birth": self.date_of_birth
        }

   

