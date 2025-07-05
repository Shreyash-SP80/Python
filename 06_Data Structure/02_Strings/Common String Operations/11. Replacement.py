# Replacement:
# Replaces substrings matching a regular expression pattern (more flexible than replace()).

# Syntax (requires import re):
#   re.sub(pattern, repl, string, count=0, flags=0)
# pattern: Regex pattern to match
# repl: Replacement string (or function)
# count: Max replacements (default: all)
# flags: Regex flags (e.g., re.IGNORECASE)

import re

text = "Python3 is better than Python2"

# Replace all digits with "X"
print(re.sub(r"\d", "X", text))
# Output: "PythonX is better than PythonX"

# Case-insensitive replacement
print(re.sub(r"python", "Java", text, flags=re.IGNORECASE))
# Output: "Java3 is better than Java2"

# Replace using a function
def to_upper(match):
    return match.group(0).upper()

print(re.sub(r"python", to_upper, text, flags=re.IGNORECASE))
# Output: "PYTHON3 is better than PYTHON2"


# 1. str.replace() - Basic Replacement
#    Replaces all occurrences of a substring with another substring.
# Syntax:
#    string.replace(old, new, count=-1)
# old: Substring to be replaced
# new: New substring to insert
# count: Maximum number of replacements (optional, default: all)

text = "I like apples, apples are tasty"
print(text.replace("apples", "oranges"))
# Output: "I like oranges, oranges are tasty"

# Replace only the first occurrence
print(text.replace("apples", "oranges", 1))
# Output: "I like oranges, apples are tasty"