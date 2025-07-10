import os

def create_sample_binary_file():
    """Create a sample binary file for demonstrations"""

    with open("sample.bin", "wb") as f:
        f.write(b'\x01\x02\x03\x04\x05')  # Sample binary data

def demonstrate_rb_mode():
    """rb mode: Read binary (file must exist)"""
    print("\n=== rb Mode: Read Binary ===")

    try:
        with open("sample.bin", "rb") as f:
            data = f.read(3)  # Read first 3 bytes
            print(f"Read data: {data}")  # b'\x01\x02\x03'
            print(f"Current position: {f.tell()}")  # 3
    except FileNotFoundError:
        print("Error: File doesn't exist")

def demonstrate_wb_mode():
    """wb mode: Write binary (overwrites)"""
    print("\n=== wb Mode: Write Binary ===")

    with open("output.bin", "wb") as f:
        f.write(b'\x41\x42\x43')  # ABC in binary
        print("Created new binary file with 'wb'")

def demonstrate_ab_mode():
    """ab mode: Append binary"""
    print("\n=== ab Mode: Append Binary ===")

    with open("output.bin", "ab") as f:
        f.write(b'\x44\x45\x46')  # DEF in binary
        print("Appended data to binary file")

def demonstrate_rb_plus_mode():
    """rb+ mode: Read/write binary (file must exist)"""
    print("\n=== rb+ Mode: Read/Write Binary ===")
    
    try:
        with open("sample.bin", "rb+") as f:
            print(f"Original first byte: {f.read(1)}")  # b'\x01'
            f.write(b'\xFF')  # Modify second byte
            f.seek(1)
            print(f"Modified second byte: {f.read(1)}")  # b'\xFF'
    except FileNotFoundError:
        print("Error: File doesn't exist")

def demonstrate_wb_plus_mode():
    """wb+ mode: Write/read binary (truncates)"""
    print("\n=== wb+ Mode: Write/Read Binary (truncates) ===")
    
    with open("wb_plus.bin", "wb+") as f:
        f.write(b'\x61\x62\x63')  # abc in binary
        f.seek(0)
        print(f"File content: {f.read()}")  # b'abc'

def demonstrate_ab_plus_mode():
    """ab+ mode: Append/read binary"""
    print("\n=== ab+ Mode: Append/Read Binary ===")
    
    with open("ab_plus.bin", "ab+") as f:
        f.write(b'\x31\x32\x33')  # 123 in binary
        f.seek(0)
        print(f"Full content: {f.read()}")  # Includes previous writes

def demonstrate_xb_mode():
    """xb mode: Exclusive binary creation"""
    print("\n=== xb Mode: Exclusive Binary Creation ===")
    
    try:
        with open("new_exclusive.bin", "xb") as f:
            f.write(b'\xAA\xBB\xCC')
            print("Exclusive binary file created")
    except FileExistsError:
        print("Error: File already exists")

def demonstrate_xb_plus_mode():
    """xb+ mode: Exclusive binary read/write"""
    print("\n=== xb+ Mode: Exclusive Binary Read/Write ===")
    
    try:
        with open("new_exclusive_rw.bin", "xb+") as f:
            f.write(b'\xDE\xAD\xBE\xEF')
            f.seek(0)
            print(f"File content: {f.read()}")
    except FileExistsError:
        print("Error: File already exists")

def main():
    # Setup initial files
    create_sample_binary_file()
    
    # Demonstrate each binary mode
    demonstrate_rb_mode()
    demonstrate_wb_mode()
    demonstrate_ab_mode()
    demonstrate_rb_plus_mode()
    demonstrate_wb_plus_mode()
    demonstrate_ab_plus_mode()
    demonstrate_xb_mode()
    demonstrate_xb_plus_mode()
    
    # Clean up (optional)
    for fname in ["sample.bin", "output.bin", "wb_plus.bin", 
                 "ab_plus.bin", "new_exclusive.bin", "new_exclusive_rw.bin"]:
        if os.path.exists(fname):
            os.remove(fname)

if __name__ == "__main__":
    main()

# Output
# === rb Mode: Read Binary ===
# Read data: b'\x01\x02\x03'
# Current position: 3

# === wb Mode: Write Binary ===
# Created new binary file with 'wb'

# === ab Mode: Append Binary ===
# Appended data to binary file

# === rb+ Mode: Read/Write Binary ===
# Original first byte: b'\x01'
# Modified second byte: b'\xff'

# === wb+ Mode: Write/Read Binary (truncates) ===
# File content: b'abc'

# === ab+ Mode: Append/Read Binary ===
# Full content: b'123'

# === xb Mode: Exclusive Binary Creation ===
# Exclusive binary file created

# === xb+ Mode: Exclusive Binary Read/Write ===
# File content: b'\xde\xad\xbe\xef'