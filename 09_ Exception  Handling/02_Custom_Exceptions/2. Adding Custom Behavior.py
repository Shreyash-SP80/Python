# A. Custom Initialization

class PaymentError(Exception):
    def __init__(self, message, transaction_id):
        super().__init__(message)
        self.transaction_id = transaction_id

try:
    raise PaymentError("Payment failed", "txn_12345")
except PaymentError as e:
    print(f"{e} (Transaction ID: {e.transaction_id})")

# Output:
# Payment failed (Transaction ID: txn_12345)


# B. Custom Attributes
from datetime import datetime  # Correct import

class APIError(Exception):
    def __init__(self, message, status_code):
        super().__init__(message)
        self.status_code = status_code
        self.timestamp = datetime.now()  # Now this will work

try:
    raise APIError("Service unavailable", 503)
except APIError as e:
    print(f"Error {e.status_code} at {e.timestamp}: {e}")

# Output:
# Error 503 at 2025-05-24 16:58:02.195054: Service unavailable


# C. With Default Messages
class EmptyCartError(Exception):
    def __init__(self, message="Shopping cart is empty"):
        super().__init__(message)

# Usage
raise EmptyCartError()  # Uses default message
raise EmptyCartError("Your cart has no items")  # Custom message