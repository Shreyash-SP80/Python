# Explanation:
# - Functions that have no parameters and no return value are the simplest type of functions in Python. 
#   They perform an action but don't accept any input or provide any output.

# Key Characteristics:
# - No Parameters: The function doesn't accept any arguments
# - No Return Value: The function doesn't return anything (implicitly returns None)
# - Side Effects: Typically used for operations that produce side effects (like printing, modifying global variables, or file operations)

# Syntax:
#   def function_name():
#       """docstring"""
#       # function body
#       # no return statement

# Example:

def greet():
    """Prints a greeting message"""
    print("Hello, World!")

# Calling the function
greet()     # Output: Hello, World!