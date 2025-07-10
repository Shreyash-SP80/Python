# Write a function that checks if a given number is prime using a loop and conditional statements.

def  Prime_check(num):

    for i in range (2, num-1):
        if (num % i == 0):
            print("{} is not Prime number..".format(num))
            return
    print("{} is Prime number..".format(num))


if __name__ == "__main__":
    num = int(input("Enter any number to check Prime or not: "))
    Prime_check(num)
