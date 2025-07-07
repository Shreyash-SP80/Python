# Positional Arguments
# The most basic way to pass arguments - matched by position.

def greet(name, message):
    print(f"{message}, {name}!")

greet("Alice", "Hello")  # "Hello, Alice!"


# Characteristics:
# Arguments are matched in order
# Number of arguments must match
# Simplest form of parameter passing