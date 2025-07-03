# Used to compare object memory locations:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)      # True (same object)
print(x is y)      # False (same content but different objects)
print(x == y)      # True (same content)
print(x is not y)  # True