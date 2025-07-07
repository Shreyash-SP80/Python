class Demo:
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return str(self.message)

obj = Demo("Hello")
print(obj)

obj1 = Demo("Heyy")
print(obj1)

# Output:
# Hello
# Heyy