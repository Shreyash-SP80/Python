# = Steps to Perform File Operations

# Step 1: Opening a File
#   By using open function we can open a 

#  => open()
# Working:
#  - Creates a file object and establishes connection to the file
#  - filename: Path to file (absolute/relative)
#  - mode: Specifies operation (read/write/append)
#  - Returns a file object that can be used for subsequent operations
#  - If file is present then it can open it if not present then create new file and open (according to mode)

# Syntax:
# file_object = open(filename, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# 1. Required Parameters
# filename
# Purpose: Path to the file (string)
# Types:
#   Relative path ("data.txt")
#   Absolute path ("/home/user/data.txt")
#   Windows path (r"C:\Users\file.txt")

# 2. Mode Parameter (mode)
# Default: 'r' (read text mode)
# Options:
# 'r': Read (default)
# 'w': Write (truncates)
# 'a': Append
# 'x': Exclusive creation
# 'b': Binary mode
# 't': Text mode (default)
# '+': Read/write mode

# 3. Advanced Parameters
# buffering
# Purpose: Controls buffering policy
# Values:
# 0: No buffering (binary only)
# 1: Line buffering (text only)
# >1: Buffer size in bytes
# -1: Default system buffering (usually 4096/8192 bytes)

# encoding
# Purpose: Text encoding for reading/writing
# Common Values:
# 'utf-8' (recommended default)
# 'ascii'
# 'latin-1'
# None: Default system encoding (platform dependent)
# Important: Only used in text mode

# errors
# Purpose: How to handle encoding/decoding errors
# Common Values:
# 'strict': Raise error (default)
# 'ignore': Skip malformed data
# 'replace': Use replacement marker (�)
# 'backslashreplace': Use \xNN escape sequences

# newline
# Purpose: Controls universal newlines
# Values:
# None: Universal newlines (convert all to \n)
# '': No conversion (raw newlines)
# '\n', '\r', '\r\n': Force specific newline

# closefd
# Purpose: Close underlying file descriptor
# Values:
# True: Close file when done (default)
# False: Leave file descriptor open
# Use Case: When passing an existing file descriptor

# opener
# Purpose: Custom file opener
# Format: Callable (file, flags) -> file descriptor
# Advanced Use: Custom file opening logic


# Example:
file = open("data.txt", "r")  # Open for reading



# Step 2: Performing Operations

# 1) Reading

#  => read()
# Working:
# By using read function we can read the data from file
# Reads entire file if size not specified
# If size is given, reads specified number of bytes/characters
# Returns content as string (text mode) or bytes object (binary mode)

# Note:
#   File must be present other wise it gives error

# Syntax:
#  file_object.read(size=-1)

# Example:
with open("data.txt", "r") as f:
    content = f.read()  # Reads entire file


#  => readline()
# Working:
# This function is used to read single line from file
# Reads single line from file
# Includes newline character at end
# Optional size parameter limits characters read
# Returns empty string at EOF

# Syntax:
#  data = file_object.readline() 

# Example:
with open("data.txt", "r") as f:
    line = f.readline()  # Reads first line


#  => readlines()
# Working:
# This function is used to read multiple lines form file (specified no. of lines)
# Reads all lines into a list
# Each list item is one line (including newline)
# Optional hint limits lines read based on size

# Syntax:
#  data = file_object.readlines(hint=-1)

# Example:
with open("data.txt", "r") as f:
    lines = f.readlines()  # All lines as list



# 2) Writing

#  => write()
# Working:
# This function is used to write the data into file text/binary
# Writes string to file
# Returns number of characters/bytes written
# In text mode, writes strings
# In binary mode, writes bytes-like objects

# Syntax:
#   file_object.write(string)

# Example:
with open("output.txt", "w") as f:
    f.write("Hello World\n")  # Writes string


#  => writelines()

# Working:
# Writes sequence of strings to file
# Sequence can be list, tuple, etc.
# Doesn't add newlines - include them in strings

# Syntax:
#  file_object.writelines(sequence)

# Example:
lines = ["First line\n", "Second line\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)  # Writes all lines



# Step 3: Closing the File

#  => close()
# Working:
# Flushes any unwritten data
# Closes the file
# Releases system resources
# Subsequent operations will raise ValueError

# Syntax:
#  file_object.close()