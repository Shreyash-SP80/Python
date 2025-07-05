# Basic unpacking
point = (10, 20)
x, y = point  # x=10, y=20

# Extended unpacking
values = (1, 2, 3, 4, 5)
first, *middle, last = values  # first=1, middle=[2,3,4], last=5

# The asterisk (*) in Python tuple unpacking is called the "iterable unpacking operator" or "star operator"

values = (1, 2, 3, 4, 5)
first, *middle, last = values

# What This Code Does
# first gets the first element (1)
# last gets the last element (5)
# *middle collects all remaining elements in the middle as a list ([2, 3, 4])