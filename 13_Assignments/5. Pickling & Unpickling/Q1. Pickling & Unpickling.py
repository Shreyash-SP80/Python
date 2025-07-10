# Create a dictionary employee = {"name": "Alice", "age": 30, "salary": 75000}
# Pickle it into employee.pkl
# Unpickle and print the data

import pickle

employee = {"name": "Alice", "age": 30, "salary": 75000}

with open("employee.pkl", 'wb') as file:
    pickle.dump(employee, file)

with open("employee.pkl", 'rb') as file:
    contect = pickle.load(file)
    print(contect)     # {'name': 'Alice', 'age': 30, 'salary': 75000}