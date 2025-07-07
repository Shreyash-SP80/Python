# Exception Handling Blocks Explained:

# A. try Block
# Contains code that might raise exceptions
# Python attempts to execute this code first

# Syntax:
# try:
#     result = 10 / 0  # This will raise ZeroDivisionError


# B. except Block
# Catches and handles specific exceptions
# Multiple except blocks can handle different exceptions
# This block comes after try block

# Syntax:
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# except TypeError:
#     print("Wrong data type used!")


# C. else Block (Optional)
# Executes only if no exceptions occurred in try
# Useful for code that should run only on success
# This block comes  after try and all the exception block

# Syntax:
# else:
    # print("Division successful:", result)


# D. finally Block (Optional)
# Always executes, whether an exception occurred or not
# Used for cleanup operations (closing files, connections)
# This block comes at  the last

# Syntax:
# finally:
    # print("This always runs")


# Note:
# Every try block can have at list oen except block

# Example 1: Basic Exception Handling
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old")
except ValueError:
    print("Please enter a valid number!")

# Output:
# Enter your age: age
# Please enter a valid number!

# Enter your age: 10
# You are 10 years old


# Example 2: Multiple Exception Types
try:
    file = open("data.txt")
    data = file.read()
    value = int(data)
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("File contains non-numeric data")
else:
    print("Successfully read value:", value)
finally:
    print("I am finally block")

# Output:
# File not found
# I am finally block
