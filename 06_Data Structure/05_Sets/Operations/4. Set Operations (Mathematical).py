
# Union (|)
a = {1, 2}; b = {2, 3}
print(a | b)  # {1, 2, 3}
print(a.union(b))


# Intersection (&)
print(a & b)  # {2}
print(a.intersection(b))


# Difference (-)
print(a - b)  # {1} (elements in a not in b)
print(a.difference(b))


# Symmetric Difference (^)
print(a ^ b)  # {1, 3} (elements in either but not both)
print(a.symmetric_difference(b))