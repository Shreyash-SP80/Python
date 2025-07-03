# input() always returns a string, you often need to convert it:

# a) int() for Numbers

age = int(input("Enter your age: "))
print(f"You will be {age + 10} in 10 years.")

# Output:
# Enter your age: 20
# You will be 30 in 10 years.


# b) float() for Decimals

price = float(input("Enter price: $"))
print(f"Total with tax: ${price * 1.1:.2f}")

# Output:
# Enter price: $20.200
# Total with tax: $22.22


# c) eval() (Use with Caution!)
# Converts input to the correct type automatically.
# Warning: Avoid eval() with untrusted input (security risk).

user_data = eval(input("Enter a value: "))  # Can be int, float, list, etc.
print(type(user_data))


# Handling Multiple Inputs
# a) split() for Space-Separated Values
x, y = input("Enter two numbers: ").split()
print(f"Sum: {int(x) + int(y)}")
# print(type(x))   (str)

# b) Using List Comprehensions
list1 = [x for x in input("Enter any numbers (Space seperated values): ").split()]
print(f"Maximum number: {max(list1)}")