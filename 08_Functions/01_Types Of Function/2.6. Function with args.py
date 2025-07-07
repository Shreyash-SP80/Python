# Explanation:
# - Variable-length arguments allow a function to accept any number of positional arguments. 
#   These are collected into a tuple inside the function.

# Key Features
# ✔ Collects extra positional arguments into a tuple
# ✔ *args must come after regular parameters
# ✔ The name args is convention (you can use any name, e.g., *numbers)
# ✔ Useful for flexible function definitions

# Syntax:
# def function_name(para1, *args):
#     """Accepts any number of positional arguments"""
#     # args is a tuple containing all passed arguments
#     return result

# Example 1: 
def sum_all(*numbers):
    """Returns the sum of all given numbers"""
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))        # 6
print(sum_all(5, 10, 15, 20))   # 50


# Example 2: Mixed Regular and *args Parameters
def greet(user, *messages):
    """Greets a user with multiple messages"""
    print(f"Hello, {user}!")
    for msg in messages:
        print(f"-> {msg}")

greet("Shreyash", "Welcome!", "How are you?")

# Output:
# Hello, Shreyash!
# -> Welcome!
# -> How are you?