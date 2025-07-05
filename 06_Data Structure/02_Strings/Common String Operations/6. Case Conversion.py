# Case Conversion:
# - Python provides several built-in methods to change the case of strings. 
# - These methods return a new string (since strings are immutable) and do not modify the original string.

s = "Python Programming"

# 1. str.lower()
#   Converts all characters in a string to lowercase.
# Syntax:
#   string.lower()

print(s.lower())       # python programming


# 2. str.upper()
#    Converts all characters in a string to uppercase.
# Syntax:
#    string.upper()

print(s.upper())       # PYTHON PROGRAMMING


# 3. str.title()
#    Converts the first letter of each word to uppercase and the rest to lowercase.
# Syntax:
#    string.title()

print(s.title())       # Python Programming


# 4. str.capitalize()
#    Converts only the first character of the string to uppercase and the rest to lowercase.
# Syntax:
#    string.capitalize()

print(s.capitalize())  # Python programming


# 5. str.swapcase()
#     Swaps the case of all characters in the string (uppercase becomes lowercase and vice versa).
# Syntax:
#     string.swapcase()

print(s.swapcase())    # pYTHON pROGRAMMING