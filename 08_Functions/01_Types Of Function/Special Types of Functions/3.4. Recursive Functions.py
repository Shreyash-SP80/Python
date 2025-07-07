# Explanation:
# A recursive function is a function that calls itself to solve smaller instances of the same problem. It consists of:
# - Base Case – A condition to stop recursion (prevents infinite loops).
# - Recursive Case – The function calls itself with a modified input.

# Syntax of a Recursive Function
# def recursive_function(params):
#     # Base case (termination condition)
#     if base_case_condition:
#         return base_case_value
    
#     # Recursive case (function calls itself)
#     return recursive_function(modified_params)

# Key Features of Recursion
# ✔ Self-referential – Calls itself
# ✔ Stack-based – Uses the call stack to manage function calls
# ✔ Divide & Conquer – Breaks problems into smaller subproblems
# ✔ Memory Intensive – Each call adds a new stack frame

# Example 1: Factorial Calculation
def factorial(n):
    # Base case: 0! = 1 or 1! = 1
    if n == 0 or n == 1:
        return 1
    
    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120 (5! = 5*4*3*2*1


# Example 2: Fibonacci Sequence
def fibonacci(n):
    # Base case: fib(0) = 0, fib(1) = 1
    if n <= 1:
        return n
    
    # Recursive case: fib(n) = fib(n-1) + fib(n-2)
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8 (0,1,1,2,3,5,8)


# Example 3: Sum of Digits
def sum_digits(n):
    # Base case: single-digit number
    if n < 10:
        return n
    
    # Recursive case: last digit + sum of remaining digits
    return (n % 10) + sum_digits(n // 10)

print(sum_digits(1234))  # Output: 10 (1+2+3+4)