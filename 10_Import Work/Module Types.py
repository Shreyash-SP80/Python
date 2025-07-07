# A. Python Files (.py)

# mymodule.py
def hello():
    print("Hello!")
    
# main.py
# import mymodule
# mymodule.hello()


# B. Compiled Python (.pyc)
# Cached bytecode files for faster imports


# C. Built-in Modules
# Written in C and compiled into Python interpreter (like sys, math)


# D. Packages (Directories)
# mypackage/
#     __init__.py
#     module1.py
#     module2.py

# Import that package into program
# Come outside  mypackage folder
# Create file were you want to  access package
#  Import packge by using follwing ways
#     from package_name import module_name
#     import package_name.module_name.*


# Dynamic Imports
module_name = "math"
math = __import__(module_name)
