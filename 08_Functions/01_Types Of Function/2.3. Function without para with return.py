# Explanation:
# - Functions that take no parameters but return a value are used when you need to:
# - Compute or generate a value without requiring any input
# - Retrieve data from an external source (like a database or file)
# - Provide configuration values or constants
# - Implement calculations that don't depend on external inputs

# Key Characteristics:
# - No Parameters: The function doesn't accept any arguments
# - With Return Value: Explicitly returns data using the return statement
# - Deterministic or Non-Deterministic: May return the same value each time (deterministic) or different values (non-deterministic)

# Syntax:
#   def function_name():
#       """docstring"""
#       # function body
#       return value

# Example:
def get_current_temperature():
    """Returns the current temperature (simulated)"""
    # In a real application, this might read from a sensor
    return 72.5  # Return a fixed value for demonstration

# Calling the function
temp = get_current_temperature()
print(f"Current temperature is {temp}°F")

# Output:
# Current temperature is 72.5°F