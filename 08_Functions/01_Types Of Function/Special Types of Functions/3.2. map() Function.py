# map() Function
# The map() function applies a given function to each item of an iterable (list, tuple, etc.) and returns a map object (an iterator).

# Syntax:
#   map(function, iterable)

# Key Features
# ✔ Applies a function to every element in an iterable
# ✔ Returns a map object (convert to list/tuple to see values)
# ✔ Works with lambda functions and regular functions
# ✔ More efficient than loops for simple transformations


# Example 1: Using map() with Lambda
numbers = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16]


# Example 2: Using map() with a Named Function
def to_upper(text):
    return text.upper()

words = ["hello", "world"]
upper_words = map(to_upper, words)
print(list(upper_words))  # Output: ['HELLO', 'WORLD']


# Example 3: map() with Multiple Iterables
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sums = map(lambda x, y: x + y, nums1, nums2)
print(list(sums))  # Output: [5, 7, 9]