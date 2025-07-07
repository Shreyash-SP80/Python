# Explanation:
# A generator function is a special kind of function that returns an iterator (a generator object) instead of a single value. 
# It uses yield instead of return to pause execution and resume later, making it memory-efficient for large datasets.

# Key Features
# ✔ Lazy Evaluation – Produces values on-demand (saves memory)
# ✔ Stateful – Remembers its state between calls
# ✔ Iterable – Can be used in for loops or with next()
# ✔ Memory Efficient – Doesn’t store all values in memory at once

# Syntax:
# def generator_function(args):
#     # Initialization
#     while condition:
#         yield value  # Pauses here and returns value
#         # Update state

# How Generators Work
# When called, a generator returns a generator object (doesn’t execute immediately).
# On next(), it runs until yield, then pauses.
# On the next next(), it resumes from where it paused.
# Raises StopIteration when done.


# Example 1: Basic Generator
def count_up_to(max):
    count = 1
    while count <= max:
        yield count  # Pauses here
        count += 1

counter = count_up_to(3)
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3
# print(next(counter))  # Raises StopIteration


# Using in a for loop:
for num in count_up_to(5):
    print(num)  # 1, 2, 3, 4, 5


# Example 2: Infinite Generator
def infinite_counter():
    num = 0
    while True:  # Runs forever!
        yield num
        num += 1

gen = infinite_counter()
print(next(gen))  # 0
print(next(gen))  # 1
# ... continues infinitely


# Example 3: Generator for Fibonacci Sequence
def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_gen()
for _ in range(10):
    print(next(fib))  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34