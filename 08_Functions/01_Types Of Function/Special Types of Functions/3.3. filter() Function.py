# Explanation:
# The filter() function constructs an iterator from elements of an iterable for which a function returns True.
# Used to filter the elements of sequences like list, dict., etc


# Syntax:
# filter(function, iterable)

# Key Features
# ✔ Filters elements based on a condition
# ✔ Returns a filter object (convert to list/tuple to see values)
# ✔ If function is None, it filters out falsy values (0, False, None, "")
# ✔ More efficient than loops for filtering


# Example 1: Using filter() with Lambda
numbers = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # Output: [2, 4, 6]


# Example 2: Using filter() with a Named Function
def is_positive(num):
    return num > 0

nums = [-2, -1, 0, 1, 2]
positives = filter(is_positive, nums)
print(list(positives))  # Output: [1, 2]


# Example 3: filter() with None (Remove Falsy Values)
values = [0, 1, False, True, "", "hello"]
truthy = filter(None, values)
print(list(truthy))  # Output: [1, True, 'hello']


# Final Example: Combining map() and filter()
numbers = [1, 2, 3, 4, 5, 6]
# Filter even numbers and square them
result = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
print(list(result))  # Output: [4, 16, 36]