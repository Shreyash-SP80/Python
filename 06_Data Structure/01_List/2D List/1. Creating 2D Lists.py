# A 2D list (or list of lists) is a matrix-like structure that stores data in rows and columns. 
# It's one of Python's most useful data structures for representing grids, tables, or game boards.

# Creating 2D Lists
# Method 1: Manual Creation

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# Method 2: Using List Comprehension
# Create a 3x3 matrix filled with zeros

rows, cols = 3, 3
matrix = [[0 for _ in range(cols)] for _ in range(rows)]


# Method 3: Using Nested Loops

matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(i * 3 + j + 1)
    matrix.append(row)
# Result: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]