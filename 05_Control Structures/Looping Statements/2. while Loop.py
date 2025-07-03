# while Loop
# Repeats a block of code as long as a condition is True.
# Syntax:
#    while condition:
       # Code to execute while condition is True

# Example 1: Basic counter
count = 0

# Loop runs as long as count < 5
while count < 5:
    print(count)  # Prints current count
    count += 1    # Increment count by 1

# Output:
# 0
# 1
# 2
# 3
# 4


# Example 2: User input validation
password = ""

# Keep asking for input until correct password is entered
while password != "secret":
    password = input("Enter password: ")
print("Access granted!")



# Example 3: Infinite loop with break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input.lower() == "quit":
        break  # Exit the loop
    print(f"You entered: {user_input}")