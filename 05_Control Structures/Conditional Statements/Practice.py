# 1. Age Category Classifier
# Write a program that categorizes a person's age group:
# Child (0-12)
# Teen (13-19)
# Adult (20-59)
# Senior (60+)


# age = int(input("Enter your age: "))
# if (age <= 12):
#     print("Child")
# elif (age <= 19):
#     print("Teenage")
# elif (age <= 50):
#     print("Adult")
# else:
#     print("Senior")



# 2. Number Analyzer
# Write a program that checks if a number is:
# Positive, negative, or zero
# Even or odd
# A single-digit or multi-digit number

# Number Analyzer Program
# Checks if a number is positive/negative/zero, even/odd, and single/multi-digit

# Get user input
num = float(input("Enter a number: "))

# Initialize result variables
sign = ""
parity = ""
digit_type = ""

# Check if positive, negative, or zero
if num > 0:
    sign = "Positive"
elif num < 0:
    sign = "Negative"
else:
    sign = "Zero"

# Check if even or odd (only for integers)
if num.is_integer():
    if int(num) % 2 == 0:
        parity = "Even"
    else:
        parity = "Odd"
else:
    parity = "Not an integer (cannot determine even/odd)"

# Check if single-digit or multi-digit
abs_num = abs(int(num)) if num.is_integer() else abs(num)
if abs_num < 10 and abs_num >= 0:
    digit_type = "Single-digit"
else:
    digit_type = "Multi-digit"

# Display results
print("\n--- Number Analysis ---")
print(f"Number: {num}")
print(f"Sign: {sign}")
print(f"Parity: {parity}")
print(f"Digit Type: {digit_type}")

# Additional checks for special cases
if num == 0:
    print("Note: Zero is neither positive nor negative")
if not num.is_integer() and parity.startswith("Not"):
    print("Note: Even/odd classification only works for integers")