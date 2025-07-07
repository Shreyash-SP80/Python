# Collects extra positional arguments into a tuple.

def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3))  # 6