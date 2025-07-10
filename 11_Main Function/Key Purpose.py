# A. Preventing Import-Time Execution
# Without this guard, all top-level code would run when imported:

# i.e  when we imoprt this file in  other program then that time __name__== "__main__" this block can not be executed
# because when imoprt __name__ is  set to module name  so this block cannot me executed (Other executed)


# Without __main__ check (bad practice)
print("This runs when imported!")  # Would execute on import

# With __main__ check (good practice)
if __name__ == "__main__":
    print("This only runs when executed directly")


# B. Creating Reusable Modules
# Allows files to work both as:
# Executable scripts when run directly
# Importable libraries when used in other code