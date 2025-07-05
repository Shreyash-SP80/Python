# Traversing a 2D List

matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

# Row-wise traversal
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()  # New line after each row

# Output :
# a b c 
# d e f 
# g h i 

# Transposing a Matrix (Rows ↔ Columns)

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)    # [['a', 'd', 'g'], ['b', 'e', 'h'], ['c', 'f', 'i']]


# Flattening a 2D List

flat_list = [item for row in matrix for item in row]
print(flat_list)    # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']