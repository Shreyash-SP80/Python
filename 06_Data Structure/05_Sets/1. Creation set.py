
# Sets are unordered collections of unique, immutable elements in Python. 
# They're optimized for membership testing and eliminating duplicate entries.
# Important Characteristics:
# - Unordered: No index positions
# - Mutable: Can add/remove items
# - Unique elements: Duplicates automatically removed
# - Only hashable types: Can't store lists/dicts (but can store tuples)

# Basic Syntax

# Empty set (note: {} creates a dict, not a set)
empty_set = set()

# Set with elements
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}

# From other iterables
from_list = set([1, 2, 2, 3])      # {1, 2, 3}
from_string = set("hello")          # {'h', 'e', 'l', 'o'}