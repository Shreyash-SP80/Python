
# Unpickling:
# Unpickling is the process of deserializing (converting the byte stream back into a Python object)
# Converts the byte stream back into a Python object.

# 1) pickle.load():
#   - It returns the pickled representation of an object from the opened file
#   - This function return the pickled representation of object from opened file

# 2) pickle.loads():
#   - It returns object hierarchy of the pickled representation of a object  
#   - This function converts the pickled representation into actual object


# Syntax:

# import pickle
# Unpickling (bytes → object)
# unpickled_object = pickle.loads(pickled_data)

# or (reading from a file)

# with open("file.pkl", "rb") as file:  # 'rb' = read binary
    # object = pickle.load(file)


# Example:
import pickle


# Pickling
data = {
    "name": "Shreyash",
    "age": 25,
    "skills": ["Python", "Data Science"]
}

pickled_bytes = pickle.dumps(data)

# Unpickle from bytes
unpickled_data = pickle.loads(pickled_bytes)
print(unpickled_data)
# Output: {'name': 'Alice', 'age': 25, 'skills': ['Python', 'Data Science']}

# Unpickle from file
with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)
    print(loaded_data)    # {'name': 'Shreyash', 'age': 25, 'skills': ['Python', 'Data Science']}