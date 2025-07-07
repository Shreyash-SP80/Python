# Explanation:
# - Default parameters allow you to define functions where some arguments have predefined values. 
#   If the caller doesn’t provide a value for these parameters, the default is used.

# Key Features:
# ✔ Optional Arguments → Callers can skip them
# ✔ Must come after non-default parameters
# ✔ Immutable defaults preferred (avoid mutable defaults like [] or {})

# Syntax:
# def function_name(param1=default1, param2=default2, ...):
#     """Docstring"""
#     # Function body
#     return result

# Example 1:
def greet(name="Guest"):
    """Greets a user (default: 'Guest')"""
    return f"Hello, {name}!"

print(greet())             # "Hello, Guest!" (uses default)
print(greet("Shreyash"))   # "Hello, Shreyash!" (overrides default)


# Example 2: 
def create_user(name, role="user", active=True):
    """Creates a user with optional role & status"""
    return {"name": name, "role": role, "active": active}

print(create_user("Shreyash")) 
# {'name': 'Shreyash', 'role': 'user', 'active': True}

print(create_user("Tanjero", "admin", False))
# {'name': 'Tanjero', 'role': 'admin', 'active': False}


# Example 3:
def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print(add_item("Apple"))   # ['Apple']
print(add_item("Banana"))  # ['Banana'] (fresh list each time)