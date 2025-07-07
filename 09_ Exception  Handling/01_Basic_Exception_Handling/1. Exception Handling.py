
# Exception handling allows you to gracefully manage errors and unexpected situations in your Python programs.

# 1. What is an Exception?
# An exception is an event that occurs during program execution that disrupts the normal flow of instructions.
#  Exceptions are raised when Python encounters an error.

# Common Built-in Exceptions:
# - ZeroDivisionError - Division by zero
# - TypeError - Operation on wrong type
# - ValueError - Invalid value
# - FileNotFoundError - File doesn't exist
# - IndexError - List index out of range
# - KeyError - Dictionary key doesn't exist
# - ImportError - Module import failed

# Basic Exception Handling Syntax

    # try:
    #     # Code that might raise an exception
    #     risky_operation()
    # except ExceptionType:
    #     # Code to handle the exception
    #     handle_error()
    # else:
    #     # Code that runs if no exception occurs
    #     do_success_work()
    # finally:
    #     # Code that always runs (cleanup)
    #     cleanup_resources()


# Example:

try:
    a = int(input("Enter 1st no.: "))
    b = int(input("Enter 2nd no.: "))
    result = a / b
    print(f"Division: {result}")
except Exception as e:  # Catches all exceptions
    print(f"An error occurred: {e}")
else:
    print("No exception occured..")
finally:
    print("I am always")

# Output:

# 1st
# Enter 1st no.: 10
# Enter 2nd no.: 0
# An error occurred: division by zero
# I am always

# 2nd
# Enter 1st no.: sh
# An error occurred: invalid literal for int() with base 10: 'sh'
# I am always

# 3rd
# Enter 1st no.: 10
# Enter 2nd no.: 20
# Division: 0.5
# No exception occured..
# I am always