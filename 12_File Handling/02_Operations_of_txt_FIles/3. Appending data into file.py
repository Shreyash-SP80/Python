
# 1st open file open()
# Use mode a
# Use write() to write the data
# close file by using close()


# By using normal syntax

file = open("data.txt", 'a')
file.write("\nI am from solapur")
print("File writed successfully..")   # File writed successfully..
file.close()

# By using with open syntax

with open("data.txt", 'a') as file:
    file.write("\nI am CS student.")
print("File writed successfully..")    # File writed successfully..