# if inside another if
num = 15
if num > 10:
    print("Greater than 10")
    if num > 20:  # Nested condition
        print("Also greater than 20")
    else:
        print("But not greater than 20")  # This will execute