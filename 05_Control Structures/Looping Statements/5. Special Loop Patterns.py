# List comprehension (with condition)
# Syntax:
#   [expression for item in iterable if condition]
# Example:
squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)   # [0, 4, 16, 36, 64]


# Dictionary comprehension
# {key: value for item in iterable if condition}

squares_dict  = {x:x**2 for x in range(10)  if x % 2 == 0}
print(squares_dict)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}


# for loop with enumerate()
# Syntax:
#   for index, value in enumerate(iterable):
       # access both index and value
for index, value in enumerate(squares):
    print(str(index) + " " + str(value))

# Output:
# 0 0
# 1 4
# 2 16
# 3 36
# 4 64
