# Explanation:
# The yield keyword is fundamental to generator functions in Python. Unlike return, which exits a function entirely, 
# yield pauses execution and remembers state, allowing the function to resume later.

# key Characteristics of yield
# ✔ Pauses Execution → Temporarily stops the function and returns a value.
# ✔ Remembers State → Resumes from where it left off when called again.
# ✔ Used in Generators → Converts a function into a generator.
# ✔ Memory Efficient → Generates values on-demand instead of storing them all at once.

# Syntax:
# def generator_function():
    # yield value  # Pauses here and returns 'value'

# How yield Works:
# When a generator function is called, it returns a generator object (does not execute immediately).
# On next(), the function runs until yield, pauses, and returns the yielded value.
# The next next() call resumes execution from where it left off.
# When the function ends, StopIteration is raised.


# Example 1: Basic Generator with yield
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
# print(next(gen))  # Raises StopIteration

# Using in a for loop:
for num in simple_generator():
    print(num)  # Output: 1, 2, 3