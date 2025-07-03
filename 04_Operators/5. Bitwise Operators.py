# Used to perform operations on binary numbers:

a = 10  # 1010 in binary
b = 4   # 0100 in binary

print(a & b)   # AND: 0 (0000)
print(a | b)   # OR: 14 (1110)
print(a ^ b)   # XOR: 14 (1110)
print(~a)      # NOT: -11 (inverts all bits)
print(a << 2)  # Left shift: 40 (101000)
print(a >> 1)  # Right shift: 5 (0101)