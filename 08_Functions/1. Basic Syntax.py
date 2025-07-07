
# Functions:
# Functions are one of the most fundamental concepts in Python programming. 
# They allow you to organize your code into reusable blocks, making your programs more modular, readable, and maintainable


# Basic Function Structure
# Syntax:

#    def function_name(parameters):
#        """docstring"""
#        # function body
#        return [expression]

# Explanation:
#  - def: Keyword to declare a function
#  - function_name: Identifier for the function
#  - parameters: Inputs to the function (optional)
#  - docstring: Documentation string (optional but recommended)
#  - return: Statement to return a value (optional)


# Example:
def greet(name):
    """This function greets the person passed as parameter"""
    print(f"Hello, {name}!")
    return f"Greeted {name}"

result = greet("Shreyash")
print(result)  # Output: Greeted Shreyash

# Output:
# Hello, Shreyash!
# Greeted Alice