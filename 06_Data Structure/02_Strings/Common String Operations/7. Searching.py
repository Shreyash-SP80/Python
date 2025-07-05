# Searching: 
# Python provides several methods to search for substrings within a string. 
# These methods help in finding the position of a substring, checking its existence, or counting occurrences.

# 1. str.find(substring)
#     Returns the lowest index where the substring is found. Returns -1 if not found.
# Syntax:
#     string.find(substring, start=0, end=len(string))
# Where, 
# substring → The text to search for.
# start (optional) → Where to start searching (default 0).
# end (optional) → Where to stop searching (default len(string)).

text = "Hello, welcome to Python programming."
print(text.find("Python"))  # Output: 18 (index where "Python" starts)
print(text.find("Java"))   # Output: -1 (not found)
print(text.find("w", 5))  # Output: 7 (finds "o" after index 5)


# 2. str.rfind(substring)
#    Same as find(), but searches from the right (end of string) and returns the highest index.
# Syntax:
#    string.rfind(substring, start=0, end=len(string))

text = "Hello world, hello Python"
print(text.rfind("hello"))  # Output: 13 (last occurrence)
print(text.rfind("Hello")) # Output: 0 (first occurrence)
print(text.rfind("Java"))  # Output: -1 (not found)


# 3. str.index(substring)
#    Works like find(), but raises a ValueError if the substring is not found.
# Syntax:
#    string.index(substring, start=0, end=len(string))

text = "Python is fun"
print(text.index("is"))   # Output: 7
print(text.index("Java")) # Raises ValueError: substring not found


# 4. str.rindex(substring)
#     Same as index(), but searches from the right (end of string).
# Syntax:
#     string.rindex(substring, start=0, end=len(string))

text = "Python is fun, Python is great"
print(text.rindex("Python"))  # Output: 17 (last occurrence)
print(text.rindex("Java"))    # Raises ValueError


# 5. substring in string (Membership Check)
#    Returns True if the substring exists, else False.
# Syntax:
#    substring in string

text = "Python programming"
print("Python" in text)  # Output: True
print("Java" in text)    # Output: False


# 6. str.startswith(prefix)
#     Checks if the string starts with a given substring.
# Syntax:
#     string.startswith(prefix, start=0, end=len(string))

text = "Python is awesome"
print(text.startswith("Python"))  # Output: True
print(text.startswith("Java"))    # Output: False


# 7. str.endswith(suffix)
#    Checks if the string ends with a given substring.
# Syntax:
#    string.endswith(suffix, start=0, end=len(string))

text = "Hello, Python"
print(text.endswith("Python"))  # Output: True
print(text.endswith("Hello"))   # Output: False


# 8. str.count(substring)
#    Counts how many times a substring appears in the string.
# Syntax:
#    string.count(substring, start=0, end=len(string))

text = "Python is easy, Python is powerful"
print(text.count("Python"))  # Output: 2
print(text.count("is"))      # Output: 2
print(text.count("Java"))    # Output: 0