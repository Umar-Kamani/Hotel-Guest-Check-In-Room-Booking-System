import os
from datetime import datetime
from .booking import Booking


class CheckInOut(Booking):
    # Payment status constants
    PAYMENT_PAID = "Paid"
    PAYMENT_NOT_PAID = "Not Paid"
    PAYMENT_PARTIAL = "Partial Payment"

VALID_PAYMENT_STATUSES = [PAYMENT_PAID, PAYMENT_NOT_PAID, PARTIAL_PAYMENT]
def __init__(self, booking_id, guest_id, room_number, status, start_date, end_date,
                 checkin_date=None, checkout_date=None, invoice_id=None, payment_status="Not Paid"):
        super().__init__(booking_id, guest_id, room_number, status, start_date, end_date)
        self.checkin_date = checkin_date
        self.checkout_date = checkout_date
        self.invoice_id = invoice_id
        self.payment_status = payment_status  # Paid, Not Paid, Partial Payment
        self.validate_payment_status()
