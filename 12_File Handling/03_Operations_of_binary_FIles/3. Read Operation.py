
# 1st open file open()
# Use mode rb
# Use read() to read the data
# close file by using close()

with open("Practice.bin", 'rb') as file:
    content = file.read()
    print(list(content))

# Output:
# [10, 20, 30, 40]

file = open("Practice.bin", 'rb')
content = file.read() 
string_content = content.decode('utf-8')
print(f"Content: {string_content}")
file.close()

# Output:
# Content: Hello bhaiI am shreyashI am shreyash

