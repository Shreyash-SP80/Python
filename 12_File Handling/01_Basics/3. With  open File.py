# with open():
# The with open() statement is Python's recommended way to handle files as it automatically manages file closing and exception handling.

# Syntax
    # with open(file, mode='r', encoding=None, errors=None, newline=None) as file_object:
        # File operations here
    # File automatically closes here

# Key Features
# ✔ Automatic closing - File is properly closed even if exceptions occur
# ✔ Cleaner code - Eliminates need for explicit close() calls
# ✔ Exception-safe - Handles errors gracefully
# ✔ Context manager protocol - Uses __enter__() and __exit__() methods

# Basic Examples
# 1. Reading a Text File
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
# File is automatically closed