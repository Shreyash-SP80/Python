# Pass sequences/dictionaries as arguments.

def point(x, y, z):
    print(f"Point at ({x}, {y}, {z})")

coordinates = (1, 2, 3)
point(*coordinates)  # Unpacks tuple

options = {'x': 4, 'y': 5, 'z': 6}
point(**options)  # Unpacks dictionary

# Output:
# Point at (1, 2, 3)
# Point at (4, 5, 6)