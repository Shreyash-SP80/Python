words = ['banana', 'apple', 'cherry']
words.sort()                    # Alphabetical: ['apple', 'banana', 'cherry']
words.sort(key=len, reverse=True) # Sort by length descending
print(words)     # ['banana', 'cherry', 'apple']