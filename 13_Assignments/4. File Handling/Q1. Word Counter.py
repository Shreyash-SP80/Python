# Read a text file (sample.txt) and count how many times a given word appears in it.

# with open("sample.txt", 'w') as file:
#     file.write("Hello bhai")

with open("sample.txt", 'r') as file:
    content = file.read()
    srch = input("Enter char to search: ")
    print(f"{srch} string appears in string at {content.count(srch)} times")
