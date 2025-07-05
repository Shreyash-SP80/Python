# Get sublists using slice notation [start:stop:step]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing
print(numbers[2:5])    # [2, 3, 4] (index 2 to 4)
print(numbers[:5])     # [0, 1, 2, 3, 4] (start to index 4)
print(numbers[5:])     # [5, 6, 7, 8, 9] (index 5 to end)

# Step slicing
print(numbers[::2])    # [0, 2, 4, 6, 8] (every 2nd element)
print(numbers[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reverse)

# Omitting indices
print(numbers[:])      # Full copy of the list