
# Explanation:
# A decorator is a design pattern in Python that allows you to modify or extend the behavior of functions or classes without permanently modifying them.

# Syntax:
# @decorator_function
# def  my_Function():
#     pass

# Key Features:
# ✔ Wraps another function
# ✔ Takes a function as input, returns a modified function
# ✔ Uses @decorator_name syntax
# ✔ Commonly used for logging, timing, access control


def  greet(func):
    def  mfx(*args, **kwargs):
        print("Good Morning!")
        func(*args, **kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def  my_Function():
    print("Hello world")

@greet
def add(a, b):
    print(f"Addition: {a+b}")

my_Function()
add(10, 20)

# greet(add)(1, 2)    If we use this syntax then we do not need to decorate function by using @
# OR

# greet(my_Function)

# Output:
# Good Morning!
# Hello world
# Thanks for using this function
# Good Morning!
# Addition: 30
# Thanks for using this function


# What Happens Here:
#  - Python sees @greet and immediately executes:
#  - my_Function = greet(my_Function)
#  - This means:
#    - The original my_Function is passed to greet()
#    - greet() returns the mfx wrapper function
#    - Now my_Function actually points to mfx (which remembers the original function)

# Calling the Decorated Function
# When you call:
#  my_Function()
#    Execution Flow:
#      mfx() is called (not the original my_Function directly)

# mfx executes:
# print("Good Morning!")                    # First print
# func(*args, **kwargs)                    # Calls original my_Function
# print("Thanks for using this function")   # Last print
# The original my_Function() runs and prints "Hello world"

# Complete Output
# Good Morning!
# Hello world
# Thanks for using this function
# Visual Representation
# Call my_Function() → mfx() → 
#     print("Good Morning!") → 
#     original my_Function() prints "Hello world" → 
#     print("Thanks...") → 
#     returns None

