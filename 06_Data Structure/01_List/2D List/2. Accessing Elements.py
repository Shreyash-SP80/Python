matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

# Access single element (row 1, column 2)
print(matrix[1][2])  # Output: 'f'

# Access entire row (row 0)
print(matrix[0])     # Output: ['a', 'b', 'c']

# Access column (column 1)
column = [row[1] for row in matrix]
print(column)        # Output: ['b', 'e', 'h']