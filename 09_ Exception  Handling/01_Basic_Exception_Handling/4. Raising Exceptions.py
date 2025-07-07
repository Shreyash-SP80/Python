# You can manually raise exceptions using raise:
# By using raise keyword we  can raise Exception at any condition


def validate_age(age):  # By using this oour own exception raised but beacuse of error program terminated
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 120:
        raise ValueError("Age seems unrealistic")
    
age = int(input("Enter your age: "))

# validate_age(age)  

# Output:
# Enter your age: -1
# Traceback (most recent call last):
#   File "d:\Programming\Python Basics\09_ Exception  Handling\01_Basic_Exception_Handling\4. Raising Exceptions.py", line 11, in <module>
#     validate_age(age)
#   File "d:\Programming\Python Basics\09_ Exception  Handling\01_Basic_Exception_Handling\4. Raising Exceptions.py", line 6, in validate_age
#     raise ValueError("Age cannot be negative")
# ValueError: Age cannot be negative

# Better way use try except block
try:
   if age < 0:
        raise ValueError("Age cannot be negative")
except Exception as e:
    print(e)

# Output:
# Enter your age: -1
# Age cannot be negative