# Custom Exception:
# Custom exceptions allow you to create application-specific error types that better represent your program's error conditions than Python's built-in exceptions.
# It means we  can create our own exception classes and raise error by using raise keyword

# 1. Why Create Custom Exceptions?
# Domain-Specific Errors: Represent errors specific to your application
# Better Error Handling: Catch specific error types rather than generic ones
# Improved Debugging: More meaningful error messages
# Code Organization: Group related errors together
# API Design: Clearer interfaces for other developers


# For defining Exception class 1st create one class name it and derive it by Exception class
# 2nd add constructor to store an exception  message  (optional)

# Basic Custom Exception Syntax
# class CustomError(Exception):
    # """Base class for custom exceptions"""
    # pass

# Example:
class InvalidEmailError(Exception):
    """Raised when an email is invalid"""
    pass

def validate_email(email):
    if "@" not in email:
        raise InvalidEmailError(f"Invalid email: {email}")

try:
    validate_email("user.example.com")
except InvalidEmailError as e:
    print(f"Error: {e}")

# Output:
# Error: Invalid email: user.example.com

