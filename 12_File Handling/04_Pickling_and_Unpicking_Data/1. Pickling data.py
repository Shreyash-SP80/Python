# Pickling and Unpickling
# - Pickling is the process of serializing (converting a Python object into a byte stream), 
#   and unpickling is the process of deserializing (converting the byte stream back into a Python object). This is useful for:
# - Saving Python objects to a file.
# - Sending Python objects over a network.
# - Storing complex data structures (lists, dictionaries, classes, etc.).


# Pickling:
# 1) pickle.dump(): 
#    - It is used to write the pickle representation of object into binary opened file
#    - This method convert the object into byte stream and write to the file (binary file)

# 2) pickle.dumps():
#    - It return the pickled representation of the object as a byte object instead of writing it to file 
#    - This method convert the object into byte stream and returns the byte stream (instead of saving to file)

# 1. Pickling (Serialization)
# Converts a Python object into a byte stream (bytes).

# Syntax:

# import pickle
# # Pickling (object → bytes)
# pickled_data = pickle.dumps(object)

# or (to save directly to a file)

# with open("file.pkl", "wb") as file:  # 'wb' = write binary
#     pickle.dump(object, file)


# Example:
import pickle

data = {
    "name": "Shreyash",
    "age": 25,
    "skills": ["Python", "Data Science"]
}

# Pickle to bytes
pickled_bytes = pickle.dumps(data)
print(pickled_bytes)  # Output: b'\x80\x04\x95...' (binary data)

# Pickle to file
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)