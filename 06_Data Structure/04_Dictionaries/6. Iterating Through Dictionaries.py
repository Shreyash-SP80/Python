student = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Physics"]
}

# By keys (default)
for key in student:
    print(key, student[key])

# Output:
# name Alice
# age 21
# courses ['Math', 'Physics']

# By items (key-value pairs)
for key, value in student.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 21
# courses: ['Math', 'Physics']