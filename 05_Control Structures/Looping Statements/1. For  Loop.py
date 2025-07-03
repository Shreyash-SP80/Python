# Loops are used to execute a block of code repeatedly.

# for Loop
# Used to iterate over a sequence (list, tuple, string, etc.) or other iterable objects.
# Syntax:
#    for item in sequence:
        # Code to execute for each item

# Example 1: Iterating through a list
fruits = ["apple", "banana", "cherry"]

# 'fruit' takes each value in 'fruits' one by one
for fruit in fruits:
    print(fruit)  # Prints each fruit in the list

# Output:
# apple
# banana
# cherry

# range():
# This function used to generate the range from given range
# Syntax:
#     range(start, end, step)
print(range(2, 20, 2))

# Example 2: Using range() for numerical iteration
# range(5) generates numbers 0 to 4
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4

# Example 3: Looping through a string
message = "Hello"
for char in message:
    print(char)  # Prints each character: H, e, l, l, o