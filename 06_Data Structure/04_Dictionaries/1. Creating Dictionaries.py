
# Dictionaries are Python's implementation of key-value pairs, providing fast lookup, insertion, and deletion operations. '
# 'They're mutable, unordered collections of items where each item is a pair of a unique key and its associated value.

# Key Characteristics:
# - Keys must be immutable (strings, numbers, tuples)
# - Values can be any type (including other dictionaries)
# - Unordered (until Python 3.7, now insertion-ordered)
# - Mutable (can change after creation)
# - Empty dictionary

empty_dict = {}

# Dictionary with key-value pairs
student = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Physics"]
}
print(student)   # {'name': 'Alice', 'age': 21, 'courses': ['Math', 'Physics']}

# Using dict() constructor
another_dict = dict(name="Bob", age=22)
print(another_dict)    # {'name': 'Bob', 'age': 22}