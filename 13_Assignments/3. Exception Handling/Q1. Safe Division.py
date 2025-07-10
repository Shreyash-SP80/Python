# Write a function that takes two numbers and returns their division. Handle exceptions for:
# Division by zero (ZeroDivisionError)
# Invalid inputs (ValueError if input is not a number)

def  Division(num1, num2):
    return num1 / num2

try:
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    print("Division: ",Division(num1, num2))
except ZeroDivisionError as a:
    print("Can not divide by zero sorry..")
except ValueError:
    print("Please enter correct value.")
else:
    print("Program exectued successfully..")
finally:
    print("Done")
    