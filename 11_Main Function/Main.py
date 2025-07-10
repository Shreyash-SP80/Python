# Understanding if __name__ == "__main__": in Python
# The if __name__ == "__main__": construct is a fundamental Python idiom that controls how code executes depending on whether a script is run directly or imported as a module.

# In other words the python code execution starts from here

# 1. What is __name__?
# __name__ is a special built-in variable that Python automatically assigns:
# When a script runs directly: __name__ is set to "__main__"
# When imported as a module: __name__ is set to the module's name


# Basic Syntax
# my_script.py
def main():
    print("This is the main function")

if __name__ == "__main__":
    main()

