# Importing the math module which provides mathematical functions
import math

# Defining constants and variables
PI = 3.14  # Approximate value of π
x, y, z = 1, 2, 0  # Multiple variable assignment

# 1. round() - Rounds a number to the nearest integer
print(round(PI))       # Output: 3 (3.14 rounds down to 3)

# 2. math.ceil() - Rounds UP to the nearest integer (ceiling function)
print(math.ceil(PI))   # Output: 4 (3.14 rounds up to 4)

# 3. math.floor() - Rounds DOWN to the nearest integer (floor function)
print(math.floor(PI))  # Output: 3 (3.14 rounds down to 3)

# 4. abs() - Returns the absolute value (magnitude without sign)
# If negative, converts to positive
print(abs(PI))         # Output: 3.14 (unchanged since already positive)
print(abs(-PI))        # Would output: 3.14

# 5. pow() - Power function (base, exponent)
print(pow(PI, 2))      # Output: 9.8596 (3.14 squared)

# 6. math.sqrt() - Square root function
print(math.sqrt(2))    # Output: 1.4142135623730951 (√2)

# 7. max() - Returns the largest value among the arguments
print(max(x, y, z))    # Output: 2 (largest of 1, 2, 0)

# 8. min() - Returns the smallest value among the arguments
print(min(x, y, z))    # Output: 0 (smallest of 1, 2, 0)

# 9. math.factorial() - Returns factorial of a number
print(math.factorial(5))  # Output: 120 (5! = 5×4×3×2×1)

# 10. math.gcd() - Greatest Common Divisor
print(math.gcd(48, 18))  # Output: 6

# 11. Constants
print(math.pi)    # 3.141592653589793
print(math.e)     # 2.718281828459045
print(math.tau)   # 6.283185307179586 (2π)
print(math.inf)   # inf
print(math.nan)   # nan