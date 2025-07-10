
# 1st open file open()
# Use mode wb
# Use write() to write the data
# close file by using close()

# By using normal syntax

list = [10, 20, 30, 40]
file = open("Practice.bin", 'wb')
barr = bytearray(list)
file.write(barr)
file.close()
print("File data written successfully..")

# Output:
# File data written successfully..

with open("Practice.bin", 'wb') as file:
    file.write(b"Hello bhai")
print("File data written successfully..")

# Output:
# File data written successfully..