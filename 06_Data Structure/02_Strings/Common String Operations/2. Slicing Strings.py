# Slicing:
# - String slicing allows you to extract a portion (substring) of a string by specifying a range of indices

# Syntax:
#   string[start:stop:step]

# Where:
#  - start: Index where the slice begins (inclusive)
#  - stop: Index where the slice ends (exclusive)
#  - step: Interval between characters (optional, default is 1) 

# key Characteristics of Slicing
#    - Positive indices count from the left (starting at 0)
#    - Negative indices count from the right (starting at -1)
#    - If omitted:
#        start defaults to 0
#        stop defaults to the end of the string
#        step defaults to 1

s = "Python Programming"

# Get characters from index 0 to 5 (exclusive)
print(s[0:6])   # 'Python'

# Omitting start (starts from beginning)
print(s[:6])    # 'Python'

# Omitting stop (goes to end)
print(s[7:])    # 'Programming'

# Get every second character
print(s[::2])   # 'Pto rgamn'


# Last 4 characters
print(s[-4:])   # 'ming'

# From 7th from end to 3rd from end
print(s[-7:-3]) # 'gram'