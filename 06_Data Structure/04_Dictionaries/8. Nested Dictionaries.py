employees = {
    "Alice": {"position": "Manager", "salary": 80000},
    "Bob": {"position": "Developer", "salary": 70000}
}

# Access nested values
print(employees["Alice"]["salary"])  # 80000
print(employees)  # {'Alice': {'position': 'Manager', 'salary': 80000}, 'Bob': {'position': 'Developer', 'salary': 70000}}