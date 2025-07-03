# Assignment expression (Python 3.8+):
# The walrus operator (:=), officially called the assignment expression operator, was introduced in Python 3.8 (PEP 572). 
# It allows you to assign values to variables as part of an expression.

# Key Characteristics
# Assignment within expressions: Performs assignment while evaluating the expression
# Returns the assigned value: The expression evaluates to the value that was assigned
# Local scope: Creates the variable in the current scope


# Without walrus
n = len("hello")
if n > 3:
    print(n)

# With walrus
if (n := len("hello")) > 3:
    print(n)  # 5


# Traditional way
while True:
    user_input = input("Enter something (or 'quit' to exit): ")
    if user_input == "quit":
        break
    print(f"You entered: {user_input}")

# With walrus
while (user_input := input("Enter something (or 'quit' to exit): ")) != "quit":
    print(f"You entered: {user_input}")
    
# Output =>
# Enter something (or 'quit' to exit): hi
# You entered: hi
# Enter something (or 'quit' to exit): quit


