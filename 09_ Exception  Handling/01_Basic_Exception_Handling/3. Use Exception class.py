# Example: Catching All Exceptions (Not Recommended)
# In this instead of defining all the exception class we can define one which can handle all the types of exception

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