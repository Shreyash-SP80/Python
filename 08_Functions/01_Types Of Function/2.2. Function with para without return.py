# Explanation:
# - Functions that accept parameters but don't return a value are used when you need to:
# - Perform an action that depends on input values
# - Modify external state or produce side effects
# - Execute operations where the result doesn't need to be captured

# Key Characteristics:
# - With Parameters: Accepts one or more input values
# - No Return Value: Doesn't use a return statement (implicitly returns None)
# - Side Effects: Typically produces visible effects (printing, file operations, modifying global variables)


# Syntax:
#   def function_name(parameter1, parameter2, ...):
#       """docstring"""
#       # function body using parameters
#       # no return statement

# Example:
def print_person_info(name, age):
    """Prints information about a person"""
    print(f"Name: {name}")
    print(f"Age: {age}")

# Calling the function
print_person_info("Shreyash", 30)

# Output:
# Name: Shreyash
# Age: 30