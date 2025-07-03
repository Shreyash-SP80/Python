# 2. Sequence Types
# Ordered collections of items.

#    a) str (String)
#     Immutable sequence of Unicode characters

text = "Hello"
multiline = """Line 1
Line 2"""

#    b) list
#     Mutable, ordered sequence
#     Can contain mixed types

fruits = ["apple", "banana", "cherry"]
mixed = [1, "two", 3.0, True]

#    c) tuple
#     Immutable, ordered sequence
#     Faster than lists

coordinates = (10.0, 20.5)
single_item = (42,)  # Note the comma