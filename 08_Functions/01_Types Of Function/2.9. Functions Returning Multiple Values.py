# Explanation:
# - In Python, functions can return multiple values in a single return statement. 
#   These values are packed into a tuple and can be unpacked by the caller.

# How It Works
# - Return as Tuple: Python automatically packs multiple return values into a tuple.
# - Unpacking: The caller can unpack them into separate variables.

# Key Features:
# ✔ Returns multiple values in a single return statement
# ✔ Values are packed into a tuple (can be indexed like result[0])
# ✔ Caller can unpack into individual variables
# ✔ Works with any data type (int, str, list, dict, etc.)

# Syntax:
# def function_name():
#     # ...
#     return value1, value2, value3  # Returns a tuple (value1, value2, value3)

# # Unpacking
# var1, var2, var3 = function_name()


# Example 1:
def get_user_info():
    name = "Shreyash"
    age = 30
    role = "Admin"
    return name, age, role  # Returns a tuple

# Unpacking the returned values
user_name, user_age, user_role = get_user_info()
print(f"Name: {user_name}, Age: {user_age}, Role: {user_role}")

# Output:
# Name: Shreyash, Age: 30, Role: Admin


# Example 2: Returning Different Data Types
def analyze_list(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    max_num = max(numbers)
    min_num = min(numbers)
    return total, average, max_num, min_num

nums = [10, 20, 30, 40, 50]
sum_val, avg_val, max_val, min_val = analyze_list(nums)
print(f"Sum: {sum_val}, Avg: {avg_val}, Max: {max_val}, Min: {min_val}")

# Output:
# Sum: 150, Avg: 30.0, Max: 50, Min: 10


# Example 3: Ignoring Unwanted Return Values
# Use _ (underscore) to ignore unwanted values:

def get_coordinates():
    return 10, 20, 30  # x, y, z

x, y, _ = get_coordinates()  # Ignore z
print(f"X: {x}, Y: {y}")

# Output:
# X: 10, Y: 20


# Example 4: Returning a Dictionary for Named Values
# If you prefer named access, return a dictionary:

def get_stats(data):
    return {
        "sum": sum(data),
        "avg": sum(data) / len(data),
        "max": max(data),
        "min": min(data)
    }

stats = get_stats([5, 10, 15, 20])
print(stats)
print(f"Sum: {stats['sum']}, Avg: {stats['avg']}")

# Output:
# {'sum': 50, 'avg': 12.5, 'max': 20, 'min': 5}
# Sum: 50, Avg: 12.5
