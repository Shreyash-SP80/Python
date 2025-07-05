# Tuples are immutable sequences in Python, similar to lists but with key differences. 
# They're used to store collections of items that shouldn't be changed.
# Tuple Characteristics:
# - Immutable: Cannot be modified after creation
# - Ordered: Maintains element order
# - Indexable: Access elements via indices
# - Heterogeneous: Can store different data types
# - Hashable: Can be used as dictionary keys (unlike lists)

# Basic Syntax:

# Empty tuple
empty_tuple = ()

# Single-element tuple (note the comma)
# Without the comma, Python interprets parentheses as regular grouping operators, not tuple creators
not_a_tuple = (42)
print(type(not_a_tuple))  # <class 'int'>

single = (42,)  # Comma required

# Multiple elements
colors = ('red', 'green', 'blue')
numbers = (1, 2, 3, 4, 5)

# Without parentheses (tuple packing)
mixed = 'apple', 3.14, True