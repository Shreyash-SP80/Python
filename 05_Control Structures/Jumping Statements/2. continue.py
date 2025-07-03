# continue
# Skips the current iteration and continues with the next.

for num in range(5):
    if num == 2:
        continue  # Skip number 2
    print(num, end=" ")  # Prints 0, 1, 3, 4