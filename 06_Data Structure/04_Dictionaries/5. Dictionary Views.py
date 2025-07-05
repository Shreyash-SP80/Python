
student = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Physics"]
}

# Views dynamically reflect dictionary changes
keys = student.keys()
print(keys)    # dict_keys(['name', 'age', 'courses'])

values = student.values()
print(values)  # dict_values(['Alice', 21, ['Math', 'Physics']])

items = student.items()
print(items)   # dict_items([('name', 'Alice'), ('age', 21), ('courses', ['Math', 'Physics'])])

student["new_key"] = "value"  # Views automatically update