letters = ['a', 'b', 'c', 'd', 'e']

# Length of list
print(len(letters))      # 5


# Check if element exists
print('c' in letters)    # True
print('z' in letters)    # False


# Count occurrences
print(letters.count('b')) # 1


# Find index of element
print(letters.index('d')) # 3


# len() - Get List Length
# Returns the number of items in a list.

fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # Output: 3


# max() - Find Maximum Value
# Returns the largest item in a list (works with numbers and strings).

numbers = [5, 2, 9, 1]
print(max(numbers))  # Output: 9

words = ["cat", "apple", "zebra"]
print(max(words))   # Output: "zebra" (alphabetical order)


# min() - Find Minimum Value
# Returns the smallest item in a list.

prices = [4.99, 2.50, 9.75]
print(min(prices))  # Output: 2.5

letters = ["b", "a", "c"]
print(min(letters)) # Output: "a"


# sum() - Calculate Total
# Returns the sum of all numbers in a list.

grades = [85, 90, 78, 92]
print(sum(grades))          # Output: 345
print(sum(grades)/len(grades))  # Output: 86.25 (average)


# reverse() - Reverse List Order
# Reverses the elements in place (modifies the original list).

colors = ["red", "green", "blue"]
colors.reverse()
print(colors)  # Output: ["blue", "green", "red"]