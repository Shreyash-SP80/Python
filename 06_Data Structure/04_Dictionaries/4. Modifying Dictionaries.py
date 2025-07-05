# Adding/Updating Items

student = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Physics"]
}

student["grade"] = "A"      # Add new key
student["age"] = 22         # Update existing key
print(student)     # {'name': 'Alice', 'age': 22, 'courses': ['Math', 'Physics'], 'grade': 'A'}

# Update multiple items
student.update({"age": 23, "city": "New York"})
print(student)   # {'name': 'Alice', 'age': 23, 'courses': ['Math', 'Physics'], 'grade': 'A', 'city': 'New York'}


# Removing Items

del student["city"]         # Remove key (raises KeyError if missing)
age = student.pop("age")    # Remove and return value
student.popitem()           # Remove and return last inserted item (Python 3.7+)
student.clear()             # Empty the dictionary