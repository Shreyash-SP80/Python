# Binary Types
# For handling binary data.

#   a) bytes
#    Immutable sequence of bytes (0-255)

data = b"hello"
print(data)   # b'hello'

#   b) bytearray
#    Mutable version of bytes

mutable_data = bytearray(b"hello")
print(mutable_data)   # bytearray(b'hello')

#   c) memoryview
#    Memory-efficient view of binary data

view = memoryview(b"hello")
print(view)   # <memory at 0x00000220CF67CD00>