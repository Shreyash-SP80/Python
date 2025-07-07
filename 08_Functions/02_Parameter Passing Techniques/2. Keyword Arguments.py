# Keyword arguments allow you to pass arguments to a function by explicitly naming each parameter, rather than relying on their position.

# Syntax:
# def function_name(param1=value1, param2=value2):
#     # Function body
#     pass

# # Calling with keyword arguments
# function_name(param1=arg1, param2=arg2)

# Key Features
# ✔ Order doesn't matter - Arguments can be passed in any order
# ✔ Clarity - Makes code more readable by showing what each argument represents
# ✔ Default values - Can be combined with default parameters
# ✔ Flexibility - Can skip optional parameters

# Example 1: Basic Usage
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

# Using keyword arguments (order doesn't matter)
describe_pet(pet_name="Whiskers", animal_type="cat")
# Output: "I have a cat named Whiskers."