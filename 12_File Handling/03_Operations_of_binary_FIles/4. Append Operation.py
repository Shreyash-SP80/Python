

# 1st open file open()
# Use mode ab
# Use write() to write the data
# close file by using close()


file = open("Practice.bin", 'ab')
file.write(b"I am shreyash")
print(f"Current file cursor position: {file.tell()}")
file.close()
print("File data written successfully..")

# Output:
# Current file cursor position: 36
# File data written successfully..


# Writing (encoding)
with open("example.txt", "wb") as file:  # 'wb' = write binary
    file.write("Hello, world!".encode('utf-8'))

# Reading (decoding)
with open("example.txt", "rb") as file:  # 'rb' = read binary
    content = file.read().decode('utf-8')  

print(content)  # Output: Hello, world!

# Output:
# Hello, world!
