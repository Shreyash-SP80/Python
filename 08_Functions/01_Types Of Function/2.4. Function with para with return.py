# Explanation:
# These are the most common and versatile types of functions in Python. They:
# Accept input parameters (required or optional)
# Process the input (perform calculations, transformations, etc.)
# Return a result (single value, tuple, list, dictionary, or even another function)

# Key Characteristics:
# = Parameters
#    - Can be positional, keyword, default, variable-length (*args), or keyword-variable (**kwargs)
#    - Allow flexible input handling
# = Return Value
#    - Must use return to send back a result
#    - Can return any data type (including None if no return is given)
#    - Can return multiple values as a tuple
# = Pure vs. Impure Functions
#    - Pure: Depends only on inputs, no side effects (e.g., mathematical functions)
#    - Impure: Modifies external state (e.g., changes a global variable or writes to a file)

# Syntax:
# def function_name(param1, param2, ...):
#     """Docstring explaining the function"""
#     # Processing logic
#     return result  # Returns a computed value

def add_numbers(a, b):
    """Returns the sum of two numbers"""
    return a + b

result = add_numbers(5, 3)
print(result)  # Output: 8


