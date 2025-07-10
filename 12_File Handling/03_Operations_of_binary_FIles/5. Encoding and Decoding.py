
# Encoding and Decoding:
# In Python, encoding converts a string into bytes, while decoding converts bytes back into a string.

# Why is it Needed?
# Files and network transmissions use bytes, not strings.
# Different systems may use different encodings (utf-8, ascii, latin-1, etc.).
# Encoding ensures compatibility when storing or transmitting text.


# 1. Encoding (String → Bytes)
# Converts a string into binary data (bytes) using a specified encoding (e.g., utf-8).

# Syntax:
# encoded_data = string_variable.encode(encoding='utf-8', errors='strict')

# encoding → Specifies the encoding scheme (default: 'utf-8').
# errors → How to handle encoding errors ('strict', 'ignore', 'replace').


# Example:
text = "Hello, world!"  
binary_data = text.encode('utf-8')  # String → Bytes  
print(binary_data)  # Output: b'Hello, world!'

# Output:
# b'Hello, world!'


# 2. Decoding (Bytes → String)
# Converts bytes back into a string using the same encoding.

# Syntax:
# decoded_string = bytes_variable.decode(encoding='utf-8', errors='strict')

# encoding → Must match the encoding used earlier.
# errors → Handles decoding errors ('strict', 'ignore', 'replace').

data = binary_data.decode(encoding='utf-8')
print(data)

# Output:
# Hello, world!


# 3. Common Encodings

# Encoding	Description
# utf-8	     Most widely used (supports all Unicode)
# ascii	     Only basic English characters (0-127)
# latin-1	     Supports Western European languages
# utf-16	     Uses 2 bytes per character

# Example with Different Encodings

text = "Héllö"  

# Encoding
utf8_bytes = text.encode('utf-8')  # b'H\xc3\xa9ll\xc3\xb6'
ascii_bytes = text.encode('ascii', errors='replace')  # b'H?ll?' (replaces non-ASCII chars)

# Decoding
decoded_utf8 = utf8_bytes.decode('utf-8')  # "Héllö"
decoded_ascii = ascii_bytes.decode('ascii')  # "H?ll?"



# Practical Example (File Handling)

# Writing (encoding)
with open("example.txt", "wb") as file:  # 'wb' = write binary
    file.write("Hello, world!".encode('utf-8'))

# Reading (decoding)
with open("example.txt", "rb") as file:  # 'rb' = read binary
    content = file.read().decode('utf-8')  

print(content)  # Output: Hello, world!

# Output:
# Hello, world!