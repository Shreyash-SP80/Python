# The ternary operator provides a concise way to write simple if-else statements in a single line.
# Syntax
#   value_if_true if condition else value_if_false

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: "Adult"


# Nested Ternary (Multiple Conditions)
score = 85
grade = "A" if score >= 90 else ("B" if score >= 80 else "C")
print(grade)  # Output: "B"


# Ternary in Function Return
def is_even(num):
    return True if num % 2 == 0 else False

print(is_even(4))  # Output: True