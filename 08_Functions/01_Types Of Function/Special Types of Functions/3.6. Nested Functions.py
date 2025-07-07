# What are Nested Functions?
# Nested functions (also called inner functions) are functions defined inside another function. They:
# ✔ Are only accessible within the outer function (encapsulation)
# ✔ Can access variables from the enclosing scope (closure)
# ✔ Help organize code into logical blocks

# Syntax
# def outer_function():
#     # Outer function code
    
#     def inner_function():
#         # Inner function code
#         return value
    
#     return inner_function()  # Call inner function

# Key Features
# ✔ Encapsulation – Inner functions are hidden from the global scope
# ✔ Closures – Can access variables from the outer function
# ✔ Modularity – Break complex tasks into smaller steps
# ✔ Decorators – Used to create Python decorators


# Example 1: Basic Nested Function
def greet(name):
    # Nested function
    def format_message():
        return f"Hello, {name}!"
    
    # Call the nested function
    return format_message()     # 

print(greet("Shreyash"))  # Output: "Hello, Shreyash!"


# Example 2: Returning a Nested Function (Closure)
def multiplier(factor):
    # Inner function remembers 'factor' even after outer function exits
    def multiply(number):
        return number * factor
    return multiply  # Returns the function, doesn't call it  
    # multiplier returns the multiply function object (not its result).

double = multiplier(2)  # 'factor' becomes 2
print(double(5))  # Output: 10 (5 * 2)

triple = multiplier(3)
print(triple(5))  # Output: 15 (5 * 3)