
# Actual Parameters (Call-Side)
# Definition: The actual values passed to the function when it's called.

# Characteristics:
# Also called "arguments"
# Can be literals, variables, or expressions
# Must match the formal parameters in number and order (unless using keywords)
# Evaluated before being passed to the function

def greet(name, message):  # name and message are formal parameters
    print(f"{message}, {name}!")

greet("Alice", "Hello")  # "Alice" and "Hello" are actual parameters