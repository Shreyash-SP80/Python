numbers = {1, 2, 3, 4}
numbers.remove(3)     # Raises KeyError if missing
print(numbers)        # {1, 2, 4}

numbers.discard(5)    # No error if missing
print(numbers)        # {1, 2, 4}

popped = numbers.pop()  # Removes random element
print(numbers)          # {2, 4}

numbers.clear()       # Empties the set
print(numbers)        # set()