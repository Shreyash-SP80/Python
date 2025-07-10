# Write a recursive function to compute the factorial of a number.
# Example: factorial(5) = 120

def  Factorial(num):
    return 1 if (num <= 1) else num * Factorial(num - 1)

if __name__ == "__main__":
    num = int(input("Enter any number to find Factorial: "))
    print(f"Factorial of ({num}) = {Factorial(num)}")