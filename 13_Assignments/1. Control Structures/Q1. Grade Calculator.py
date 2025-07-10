# Write a program that takes a student's score (0-100) as input and prints their grade based on:
# - A (90-100), B (80-89), C (70-79), D (60-69), F (<60).
# - Use if-elif-else statements.

score = float(input("Enter your marks: "))

grade  = "A" if (score >= 90 and score <= 100) else ("B" if (score >= 80) else ("C" if (score >= 70) else ("D" if (score >= 60) else "Fail") ))

print(f"Your Grade is: {grade}")