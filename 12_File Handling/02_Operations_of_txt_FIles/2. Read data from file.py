
# 1st open file open()
# Use mode r
# Use read() / readline() / readlines() to read the data
# close file by using close()

# By using simple syntax

file = open("data.txt", 'r')
data = file.read()    # Reads all data
print(f"Content: {data}")
# Output:
# Content: Hello, How are you
# I am Shreyash

file.seek(0)    # move cursor at start postion
print(f"Current cursor position {file.tell()}")   # Current cursor position 0 (tells the cursor position)

data = file.read(5)   # reads 5 chars
print(f"Content: {data}")    # Content: Hello

file.seek(0)

data = file.readline()
print(f"Content: {data}")    # Content: Hello, How are you

file.seek(0)

data = file.readline(2)
print(f"Content: {data}")     # Content: He

file.seek(0)

# The readlines() method reads all lines of a file and returns them as a list of strings, where each string represents one line from the file.
data = file.readlines()
print(f"Content: {data}")  # Content: ['Hello, How are you\n', 'I am Shreyash']

print(f"Current cursor position {file.tell()}")    # Current cursor position 33
file.seek(0)

data = file.readlines(1)    # Reads single line because 1 is specified
print(f"Content: {data}")   # Content: ['Hello, How are you\n']


file.close()