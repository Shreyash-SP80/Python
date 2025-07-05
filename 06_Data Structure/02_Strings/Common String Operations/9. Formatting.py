# String Formatting:
# String formatting allows you to create dynamic strings by inserting variables/values into predefined text.


# 1. f-Strings (Python 3.6+)
#     The modern and recommended way for string formatting.
# Syntax:
#     f"Text {variable} more text"

name = "Alice"
age = 25

# Basic f-string
print(f"My name is {name} and I'm {age} years old.")
# Output: "My name is Alice and I'm 25 years old."

# Expressions inside f-strings
print(f"Next year, I'll be {age + 1} years old.")
# Output: "Next year, I'll be 26 years old."

# Formatting numbers
price = 19.99
print(f"Price: ${price:.2f}")  # 2 decimal places
# Output: "Price: $19.99"


# 2. str.format() Method
#    An older but flexible way to format strings.
# Syntax:
#    "Text {} more text".format(variable)

name = "Bob"
age = 30

# Basic usage
print("My name is {} and I'm {} years old.".format(name, age))
# Output: "My name is Bob and I'm 30 years old."

# Positional indexing
print("{1} is {0} years old.".format(age, name))
# Output: "Bob is 30 years old."

# Named arguments
print("Hello, {name}! You are {age}.".format(name="Alice", age=25))
# Output: "Hello, Alice! You are 25."

# Number formatting
print("Price: ${:.2f}".format(19.99))
# Output: "Price: $19.99"


# 3. %-formatting (Old Style)
#    Legacy method (similar to C's printf).
# Syntax:
#    "Text %s more text" % variable

name = "Charlie"
age = 35

# Basic usage
print("My name is %s and I'm %d years old." % (name, age))
# Output: "My name is Charlie and I'm 35 years old."

# Number formatting
print("Price: $%.2f" % 19.99)
# Output: "Price: $19.99"