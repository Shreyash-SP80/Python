# 1. What is a File?
#  - A file is a named location on disk that stores information permanently. 
#    Files allow data to persist even after a program terminates, enabling:
#  - Data storage beyond program execution
#  - Data sharing between programs
#  - Large data handling without using memory

# 2. Types of Files
#  A. Text Files
#    - Human-readable format (ASCII/Unicode)
#    - Contains plain text characters
#    - Examples: .txt, .csv, .html, .py
#    - Processed line by line
#    - Default mode in Python ('t')

#  B. Binary Files
#    - Non-human readable format (machine format)
#    - Contains bytes (0s and 1s)
#    - Examples: .jpg, .png, .exe, .pdf
#    - Requires special handling
#    - Use 'b' mode in Python

# 3. File Operations
#  - Core Operations
#     Opening - Establishing connection to file
#     Reading - Extracting data from file
#     Writing - Storing data to file
#     Appending - Adding to existing content
#     Closing - Terminating connection

# Additional Operations
# Seeking (changing file position)
# Renaming
# Deleting
# Checking properties