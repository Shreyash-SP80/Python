def complex_function(a, b=2, *args, **kwargs):
    """Function with all parameter types"""
    print(f"a: {a}, b: {b}")
    print("args:", args)
    print("kwargs:", kwargs)

complex_function(1, 3, 4, 5, 6, x=7, y=8)
# Output:
# a: 1, b: 3
# args: (4, 5, 6)
# kwargs: {'x': 7, 'y': 8}