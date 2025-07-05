# 1. Splitting Strings
#   str.split() - Basic Splitting
#   Divides a string into a list using a delimiter (default: whitespace).
# Syntax:
#   string.split(sep=None, maxsplit=-1)
# sep: Separator (default: any whitespace)
# maxsplit: Maximum splits (default: unlimited)

text = "Python is awesome"
print(text.split())  # ['Python', 'is', 'awesome']

csv = "apple,orange,banana"
print(csv.split(','))  # ['apple', 'orange', 'banana']

# Limit splits
print("one two three four".split(' ', maxsplit=2))  # ['one', 'two', 'three four']


# str.rsplit() - Right-Side Splitting
# Same as split(), but starts from the right.

text = "one two three four"
print(text.rsplit(' ', maxsplit=2))  # ['one two', 'three', 'four']


# str.splitlines() - Split by Lines
# Splits at line breaks (\n, \r, etc.).

multiline = "Line1\nLine2\r\nLine3"
print(multiline.splitlines())  # ['Line1', 'Line2', 'Line3']


# str.partition() & str.rpartition()
# Split into 3 parts: (before, separator, after).

email = "user@example.com"
print(email.partition('@'))  # ('user', '@', 'example.com')

# rpartition() splits from the right
path = "home/user/docs"
print(path.rpartition('/'))  # ('home/user', '/', 'docs')



# 2. Joining Strings
# str.join() - Combine Strings
# Joins an iterable (list, tuple) of strings with a separator.
# Syntax:
#   separator.join(iterable)

words = ["Python", "is", "great"]
print(' '.join(words))  # "Python is great"

# Join with different separator
print('-'.join(['2023', '12', '31']))  # "2023-12-31"

# Join characters of a string
print(':'.join("ABC"))  # "A:B:C"


text = "  Hello   world  "
cleaned = ' '.join(text.split())  # "Hello world"