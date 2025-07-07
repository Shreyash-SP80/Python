# Explanation:
# Lambda functions are small, anonymous functions defined using the lambda keyword. Unlike regular functions (def), they:
# ✔ Have no name (anonymous)
# ✔ Are written in a single line
# ✔ Cannot contain multiple statements
# ✔ Return a value automatically

# Key Features
# ✔ No return keyword (the expression is automatically returned)
# ✔ Can take multiple arguments (lambda x, y: x + y)
# ✔ Often used for short operations inside other functions
# ✔ Cannot include statements like if-else (unless in expression form)

# Syntax
# lambda arguments: expression

# Example 1: Basic Lambda Function
# Regular function
def square(x):
    return x ** 2

# Equivalent lambda
square = lambda x: x ** 2

print(square(5))  # Output: 25