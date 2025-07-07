# reduce() Function:
#  The reduce() function is a powerful functional programming tool that sequentially applies a function to items in an iterable and reduces them to a single cumulative value.

# Basic Syntax

# from functools import reduce
# reduce(function, iterable[, initializer])

# How reduce() Works
# - Takes the first two items from the iterable
# - Applies the function to them
# - Takes the result and the next item
# - Repeats until one final value remains

# Example 1:
from functools import reduce

arr = [10, 20, 30, 40, 50]
result = reduce(lambda x, y: x + y, arr)
print(result)    # 150


max = reduce(lambda x, y: x if x > y else y, arr)
print(max)   # 50

n = 5
fact = reduce(lambda x, y: x * y, range(1, n+1))
print(fact)     # 120
