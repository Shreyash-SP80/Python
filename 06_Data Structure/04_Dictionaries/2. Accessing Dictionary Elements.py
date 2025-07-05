student = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Physics"]
}

print(student["name"])  # "Alice" (raises KeyError if missing)

# Safer access with get()
print(student.get("age"))      # 21
print(student.get("grade"))    # None (instead of error)
print(student.get("grade", "N/A"))  # "N/A" (default value)