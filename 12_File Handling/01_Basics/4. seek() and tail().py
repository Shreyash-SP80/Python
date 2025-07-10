# 1. seek() Method
# Purpose
# The seek() method changes the current file position (cursor position) to a specified offset.

# Syntax:
#   file_object.seek(offset, whence=0)
# Parameters
# offset: Number of bytes to move
# whence (optional): Reference point for offset:
# -  0 (default): Beginning of file
# -  1: Current position
# -  2: End of file

# Examples
# Basic seek() usage
with open('example.txt', 'r') as file:
    file.seek(10)  # Move to 10th byte
    print(file.read(5))  # Read next 5 bytes


# Using whence parameter
with open('data.bin', 'rb') as file:
    file.seek(5, 0)  # 5 bytes from start (same as seek(5))
    file.seek(3, 1)  # 3 bytes from current position
    file.seek(-2, 2)  # 2 bytes before end of file



# 2. tell() Method
# Purpose
# The tell() method returns the current position of the file pointer (cursor).

# Syntax:
#   current_position = file_object.tell()

# Examples
# Basic tell() usage
with open('example.txt', 'r') as file:
    print(file.tell())  # 0 (start of file)
    file.read(5)
    print(file.tell())  # 5 (after reading 5 bytes)



# Combining seek() and tell()
with open('data.txt', 'r+') as file:
    position = file.tell()  # Get current position (0)
    file.seek(0, 2)  # Jump to end
    end_pos = file.tell()  # Get file size
    file.seek(0)  # Return to start