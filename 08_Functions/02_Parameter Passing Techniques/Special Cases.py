
# Forced Keyword Arguments
# Require arguments to be passed by keyword:

def connect(*, host, port):
    print(f"Connecting to {host}:{port}")

connect(host="localhost", port=5432)  # OK
connect("localhost", 5432)  # Error


# Positional-Only Parameters
# Python 3.8+ allows parameters to be positional-only:

def greet(name, /, message="Hello"):
    print(f"{message}, {name}!")

greet("Alice")  # OK
greet(name="Alice")  # Error (name is positional-only)