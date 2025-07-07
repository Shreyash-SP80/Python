# Explanation:
# **kwargs allows a function to accept any number of keyword arguments, which are collected into a dictionary inside the function.

# Key Features
# ✔ Collects extra keyword arguments into a dictionary
# ✔ **kwargs must come after all other parameters
# ✔ The name kwargs is convention (you can use any name, e.g., **options)
# ✔ Useful for flexible configuration & data passing

# Syntax:
# def function_name(para1,.., **kwargs):
#     """Accepts any number of keyword arguments"""
#     # kwargs is a dictionary containing all passed keyword args
#     return result

# Example 1: 
def build_profile(**user_info):
    """Builds a user profile dictionary"""
    return user_info

profile = build_profile(name="Shreyash", age=25, role="Admin")
print(profile)

# Output:
# {'name': 'Shreyash', 'age': 25, 'role': 'Admin'}


# Example 2: 
def process_data(name, *scores, **metadata):
    """Processes user data with scores and metadata"""
    print(f"Name: {name}")
    print(f"Scores: {scores}")
    print(f"Metadata: {metadata}")

process_data("Shreyash", 85, 92, 78, school="XYZ", grade="A")

# Output:
# Name: Shreyash
# Scores: (85, 92, 78)
# Metadata: {'school': 'XYZ', 'grade': 'A'}