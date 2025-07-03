# Syntax:
# if condition1:
#     code1
# elif condition2:
#     code2
# else:
#     default code

score = 85
if score >= 90:
    grade = "A"
elif score >= 80:  # This condition is True
    grade = "B"    # This will execute
elif score >= 70:
    grade = "C"
else:
    grade = "D"
print(grade)  # Output: B