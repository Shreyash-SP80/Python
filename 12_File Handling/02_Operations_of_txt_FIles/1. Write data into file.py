
# 1st open file open()
# Use mode w
# Use write() to write the data
# close file by using close()

# By using normal syntax

file = open("data.txt", 'w')
file.write("Hello, How are you\nI am Shreyash")
file.close()
print("File writed successfully..")

# Output:
# File writed successfully..


# By using with open function
with open("data.txt", 'w') as file:
    file.writelines("Hello, How are you\nI am Shreyash")
# File closed automatically
print("File writed successfully..")

# Output:
# File writed successfully..

with open('output.txt', 'w', encoding='utf-8') as file:
    file.write("Hello World\n")
    file.write("Second line\n")
print("File writed successfully..")   # File writed successfully..