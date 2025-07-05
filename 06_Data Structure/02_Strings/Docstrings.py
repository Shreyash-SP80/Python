# What is a Docstring?
# A docstring (documentation string) is a string literal that appears as the first statement in a module, function, class, or method definition. 
#  It serves as human-readable documentation for your code.

# In other words it provides the information about function

# Example 1:
def calculate_area(length, width):
    """Calculate and return the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    
    Returns:
        float: The computed area (length × width)
    """
    return length * width
print(calculate_area(10, 30))
print(calculate_area.__doc__)

# Output:
# 300
# Calculate and return the area of a rectangle.

#     Args:
#         length (float): The length of the rectangle
#         width (float): The width of the rectangle

#     Returns:
#         float: The computed area (length × width)


# Example 2:
def  add(a, b):
    '''
       The function takes  two arguments to calculate addition of two numbers and  return a value
    '''
    return a + b
print(add(10, 20))
print(add.__doc__)

# Output:
# 30

#     The function takes  two arguments to calculate addition of two numbers and  return a value