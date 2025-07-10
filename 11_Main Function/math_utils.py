def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print("Hello i am executed after imoprting")


# print(add(20, 30))  # This line can execute automatically when ever we imoprt this file in any  progarm this is problem to fix that we use __main__


# This above block is executed when math_utils.py file runs directly (If this file imported the not nus this block)
if __name__ == "__main__":
    # Test code only runs when executed directly
    print("Running tests:")
    print(add(5, 3))      # Output: 8
    print(subtract(5, 3)) # Output: 2
    
    #  Output:
    # Running tests:
    # 8
    # 2

