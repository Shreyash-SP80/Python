# String Validation:
#  - Python provides several built-in methods to validate the content of strings. 
#  - These methods check if a string meets certain criteria and return True or False.

# 1. str.isalpha()
#     Checks if all characters are alphabetic (a-z, A-Z).
# Syntax:
#     string.isalpha()

print("Python".isalpha())  # True
print("Python3".isalpha()) # False (contains a digit)


# 2. str.isdigit() / str.isnumeric()
#     Checks if all characters are digits (0-9).
# Syntax:
#     string.isdigit()
#     string.isnumeric()  # Also recognizes Unicode numerals (like ¾)

print("123".isdigit())   # True
print("12a".isdigit())   # False
print("¾".isnumeric())   # True (Unicode numeral)


# 3. str.isalnum()
#     Checks if all characters are alphanumeric (letters or numbers).
# Syntax:
#     string.isalnum()

print("Python3".isalnum())  # True
print("Python 3".isalnum()) # False (contains space)


# 4. str.isdecimal()
#     Checks if all characters are decimal digits (0-9).
# Syntax:
#     string.isdecimal()

print("123".isdecimal())  # True
print("12.3".isdecimal()) # False (contains a dot)


# 5. str.isspace()
#     Checks if all characters are whitespace (space, tab, newline).
# Syntax:
#     string.isspace()

print("   ".isspace())  # True
print(" a ".isspace())  # False (contains 'a')


# 6. str.islower()
#     Checks if all alphabetic characters are lowercase.
# Syntax:
#     string.islower()

print("python".islower())  # True
print("Python".islower())  # False (P is uppercase)


# 7. str.isupper()
#      Checks if all alphabetic characters are uppercase.
# Syntax:
#      string.isupper()

print("PYTHON".isupper())  # True
print("Python".isupper())  # False (contains lowercase)


# 8. str.istitle()
#     Checks if each word starts with an uppercase letter and the rest are lowercase.
# Syntax:
#     string.istitle()

print("Python Is Great".istitle())  # True
print("Python is great".istitle())  # False ("is" is lowercase)


# 9. str.isprintable()
#     Checks if all characters are printable (not escape sequences like \n, \t).
# Syntax:
#     string.isprintable()

print("Hello".isprintable())  # True
print("Hello\n".isprintable())  # False (contains \n)


# 10. str.isidentifier()
#    Checks if the string is a valid Python identifier (variable name).
# Syntax:
#    string.isidentifier()

print("var_name".isidentifier())  # True
print("123var".isidentifier())    # False (starts with a digit)